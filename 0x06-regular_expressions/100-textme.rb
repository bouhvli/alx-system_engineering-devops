#!/usr/bin/env ruby
send = ARGV[0].match(/\[from:(.*?)\]/)&.captures&.first
receive = ARGV[0].match(/\[to:(.*?)\]/)&.captures&.first
flag = ARGV[0].match(/\[flags:(.*?)\]/)&.captures&.first
puts "#{send},#{receive},#{flag}"
