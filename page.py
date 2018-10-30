page = 35  #현재 페이지 번호

#공식 1 -> 게시물 번호(시작/종료)

end_num = page * 10
start_num = end_num - 9

print(start_num, end_num)


#공식 2 -> 하단 페이지 네비게이션(페이지네이션)

start_page = (page - 1) // 10 * 10 + 1
end_page = start_page + 9

print(start_page, end_page)