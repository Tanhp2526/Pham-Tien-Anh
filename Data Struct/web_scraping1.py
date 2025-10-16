from bs4 import BeautifulSoup
import requests

html = "!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, "html.parser")

tag_object = soup.h3
tag_child = tag_object.b
parent_tag = tag_child.parent
sibling_1 = tag_object.next_sibling
print(sibling_1)