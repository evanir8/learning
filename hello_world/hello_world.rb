starts = 0
str    = ARGV.empty? ? 'Hello World Ruby' : ARGV[0]
ends   = str.size
loop do
  print "#{str[starts, ends]} #{str[0, starts]} \r"
  starts =  starts > ends ? 0 : starts+1
  sleep 0.5
end
