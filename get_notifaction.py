import requests  
from bs4 import BeautifulSoup  
import os  
import urllib.request  
  
def get_pdf_links(url):  
    response = requests.get(url)  
    soup = BeautifulSoup(response.text, 'html.parser')  
  
    pdf_links = []  
  
    for link in soup.find_all('a'):  # 查找所有超链接  
        href = link.get('href')  # 获取链接  
        if href and 'pdf' in href.lower():  # 如果链接是PDF文件  
            pdf_links.append(href)  # 添加到列表中  
  
    return pdf_links  
  
def download_pdf(pdf_links, output_dir, url_prefix):
    if not os.path.exists(output_dir):  # 如果输出目录不存在，创建它  
        os.makedirs(output_dir)
            
    for link in pdf_links:  
        url = url_prefix + link  # 请替换为实际的链接  
        filename = os.path.join(output_dir, link)  # 输出文件名，包含完整路径  
        with urllib.request.urlopen(url) as url:  
            with open(filename, 'wb') as file:  
                file.write(url.read())  # 下载文件并保存到指定路径  
  
# 测试代码  
url = "http://kjs.mof.gov.cn/zhengcefabu/202311/t20231124_3918214.htm"  # 请替换为实际的网页链接  
last_slash_index = url.rfind("/")  
field_before_last_slash = url[:last_slash_index]  
print(field_before_last_slash)
output_dir = "pdfs"  # 请替换为实际的下载文件保存路径  
pdf_links = get_pdf_links(url)  
download_pdf(pdf_links, output_dir, field_before_last_slash)