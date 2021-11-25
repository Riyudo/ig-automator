from logic import Logic


def main():
    #START
    logic = Logic()
    #haneul's pk: 47635781514
    logic.clientInfo()



    #TESTING USER.PY
    info_list = logic.get_userinfo('haneul.exe')
    user = logic.create_user(info_list)
    user.print_userinfo()


    #LOGOUT
    logic.api.logout()
    return


if __name__ == '__main__':
    main()