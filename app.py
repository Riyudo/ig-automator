from logic import Logic


def main():
    logicTest = Logic()
    #logicTest.clientInfo() haneul's pk: 47635781514
    print( logicTest.get_pk(input("Username: ")) )
    logicTest.api.logout()
    return


if __name__ == '__main__':
    main()