#!/usr/bin/env ruby
# Script to import GEO-SEO News markdown files into Jekyll _posts format
# Usage: ruby scripts/import_posts.rb --source-dir <path>

require 'fileutils'
require 'pathname'
require 'optparse'

options = {}
OptionParser.new do |opts|
  opts.banner = "Usage: ruby scripts/import_posts.rb --source-dir <path>"
  opts.on("--source-dir DIR", "Path to GEO-SEO News directory") { |v| options[:source_dir] = v }
  opts.on("--dest-dir DIR", "Path to Jekyll _posts directory") { |v| options[:dest_dir] = v }
  opts.on("-d", "--dry-run", "Show what would be done without making changes") { |v| options[:dry_run] = true }
  opts.on("-h", "--help", "Print this help") { puts opts; exit }
end.parse!

source_dir = options[:source_dir] || ENV['SOURCE_DIR']
dest_dir = options[:dest_dir] || File.join(__dir__, '..', '_posts')
dry_run = options[:dry_run]

unless source_dir && File.directory?(source_dir)
  puts "Error: --source-dir must point to an existing directory"
  puts "Usage: ruby scripts/import_posts.rb --source-dir <path>"
  exit 1
end

# Ensure destination exists
FileUtils.mkdir_p(dest_dir) unless dry_run

# Track imports
imported = 0
skipped = 0
errors = []

# Walk through source directory
Dir.glob(File.join(source_dir, '**', '*.md')).each do |file_path|
  # Skip README and config files
  basename = File.basename(file_path)
  next if basename == 'README.md' || basename == 'sources.json'
  
  # Parse relative path to extract source name and date
  rel_path = file_path.sub(File.expand_path(source_dir), '')
  parts = Pathname.new(rel_path).each_filename.to_a
  
  # Structure: <source>/<date>/<title>.md
  next if parts.length < 3
  
  source_name = parts[0]
  date_str = parts[1]
  title = parts[2].sub(/\.md$/, '')
  
  # Validate date format YYYY-MM-DD
  next unless date_str.match?(/^\d{4}-\d{2}-\d{2}$/)
  
  # Create Jekyll post filename
  slug = title.downcase.gsub(/[^a-z0-9]+/, '-').gsub(/^-+|-+$/, '')
  post_filename = "#{date_str}-#{slug}.md"
  post_path = File.join(dest_dir, post_filename)
  
  # Skip if already exists (in case of reimport)
  next if File.exist?(post_path) && !options[:force]
  
  # Read frontmatter and content
  content = File.read(file_path, encoding: 'UTF-8')
  
  # Extract frontmatter
  if content.start_with?('---')
    parts = content.split('---', 3)
    if parts.length >= 3
      frontmatter = parts[1].strip
      body = parts[2]
    else
      body = content
      frontmatter = ''
    end
  else
    body = content
    frontmatter = ''
  end
  
  # Build Jekyll frontmatter
  # Extract values from original frontmatter
  title_match = frontmatter.match(/^title:\s*"([^"]+)"/m)
  source_match = frontmatter.match(/^source:\s*"([^"]+)"/m)
  published_match = frontmatter.match(/^published:\s*([^ \n]+)/m)
  url_match = frontmatter.match(/^url:\s*"([^"]+)"/m)
  categories_match = frontmatter.match(/^categories:\s*\n(.*?)\n---/m)
  author_match = frontmatter.match(/^author:\s*"([^"]+)"/m)
  
  jekyll_title = title_match ? title_match[1] : title
  jekyll_source = source_match ? source_match[1] : source_name
  jekyll_published = published_match ? published_match[1] : date_str
  jekyll_url = url_match ? url_match[1] : ''
  jekyll_author = author_match ? author_match[1] : ''
  
  # Parse categories
  jekyll_categories = []
  if categories_match
    categories_match[1].scan(/-\s*"([^"]+)"/).each { |c| jekyll_categories << c[0] }
  end
  
  # Build new frontmatter
  new_frontmatter = "---\n"
  new_frontmatter += "layout: post\n"
  new_frontmatter += "title: \"#{jekyll_title}\"\n"
  new_frontmatter += "date: #{jekyll_published}\n"
  new_frontmatter += "source: \"#{jekyll_source}\"\n"
  if jekyll_url
    new_frontmatter += "url: \"#{jekyll_url}\"\n"
  end
  if jekyll_author
    new_frontmatter += "author: \"#{jekyll_author}\"\n"
  end
  if jekyll_categories.any?
    new_frontmatter += "categories:\n"
    jekyll_categories.each { |cat| new_frontmatter += "  - \"#{cat}\"\n" }
  end
  new_frontmatter += "---\n\n"
  
  # Write post
  new_content = new_frontmatter + body
  unless dry_run
    File.write(post_path, new_content, encoding: 'UTF-8')
  end
  
  puts "[IMPORT] #{source_name}/#{date_str}/#{title}"
  imported += 1
rescue => e
  errors << "#{file_path}: #{e.message}"
  skipped += 1
end

puts "\n#{'='*50}"
puts "Import complete:"
puts "  Imported: #{imported}"
puts "  Skipped: #{skipped}"
puts "  Errors: #{errors.length}"

unless errors.empty?
  puts "\nErrors:"
  errors.each { |e| puts "  #{e}" }
end
