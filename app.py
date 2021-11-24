from logic import Logic


def main():
    print("Before the constructor")
    logicTest = Logic()
    logicTest.welcome()
    logicTest.clientInfo()
    logicTest.api.logout()
    return


if __name__ == '__main__':
    main()