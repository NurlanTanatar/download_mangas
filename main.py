from get_files import download_files_from_report
from check_missing import check_for_missing_files
from get_links import get_links_from_website
website = str(input("url of manga from https://manga-online.biz"))
file_name = "output"
print("getting links and writing into output.txt")
get_links_from_website(website)
print("downloading") 
download_files_from_report(file_name)
print("checking")
check_for_missing_files(file_name)