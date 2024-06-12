from menu import show_menu
import student_info as si

def main():
    """输入操作"""
    while True:
        # 显示菜单
        show_menu()
        # 用户输入选择
        option = input("请选择：")
        # 根据选择处理相应的事件
        if option == 'q':
            break
        elif option == '1':
            si.add_student()
        elif option == '2':
            si.show_all_student()
        elif option == '3':
            si.add_student()
        elif option == '4':
            si.add_student()
        elif option == '5':
            si.show_order_by_score_desc()
        elif option == '6':
            si.show_order_by_score_asc()
        elif option == '7':
            si.show_order_by_age_desc()
        elif option == '8':
            si.show_order_by_age_asc()
        elif option == '9':
            si.add_student()
        elif option == '10':
            si.add_student()

main()