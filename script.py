f = open("kk_sample.txt", "r")

lines = f.readlines()

markdown = ""

output_file = open("markdown.md", "w")
output_file.write("---\n")
output_file.write("layout: post\n")
output_file.write("title: \"Kat's Kable xx\"\n")
output_file.write("description: \"\"\n")
output_file.write("date: \n")
output_file.write("tags: [kable]\n")
output_file.write("comments: false\n")
output_file.write("share: true\n")
output_file.write("---\n\n")

intro = lines[1]

markdown += intro
output_file.write(intro)

total_lines = len(lines)
waiting_for_title = 0
waiting_for_text = 0
line_count = 2
article_count = 0
max_count = 8

while line_count < total_lines:
	line = lines[line_count]
	line_count += 1
	if line == "\n":
		output_file.write("\n")
	if len(line) == 2:
		output_file.write("\n")
		output_file.write("* * *\n")
		output_file.write("**" + line[0] + "**\n")
		output_file.write("{: style=\"text-align: center;\"}\n")
		waiting_for_title = 1
		waiting_for_text = 0
		article_count += 1
		continue
	if waiting_for_title == 1:
		output_file.write("[" + line[:-1] + "]()\n\n")
		output_file.write("{: style=\"text-align: center;\"}")
		waiting_for_title = 0
		waiting_for_text = 1
		continue
	if waiting_for_text == 1:
		output_file.write(line)
		output_file.write("{: style=\"text-align: center;\"}")
