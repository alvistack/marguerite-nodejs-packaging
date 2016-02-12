#!/usr/bin/env ruby

require 'rubygems'
require 'json'
require '/usr/lib/rpm/nodejs/bundles.rb'
include Bundles

buildroot = Bundles.getbuildroot

## all directories

files = []
Dir.glob(buildroot + "/**/package.json") do |f|
	files << f
end

pkgname = ARGV[0]
dep = ARGV[1]
pkgjson = ""
json = {}

files.each do |f|
	pkgjson = f if f.index(pkgname + "/package.json")
end

# get its parent
pkgjson = pkgjson.gsub('node_modules/' + pkgname + '/package.json','') + "package.json"

File.open(pkgjson,'r:UTF-8') {|f| json = JSON.parse(f.read)}

json["dependencies"][pkgname] = dep

File.open(pkgjson,'w:UTF-8') {|f| f.write JSON.pretty_generate(json) }
