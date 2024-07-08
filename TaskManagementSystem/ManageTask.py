import System

def initiate():
    while True:
        print("1.Add a New Task\n2.Remove Particular Task\n3.Search for Existing Task\n4.Show all Existing Task\n5.Clear Log\n6.Delete all Tasks\n7.End Session\n")
        try:
            r = int(input("Enter: "))
        except:
            print("Enter only numeric characters !!!")
            r = -1
        match r:
            case 1:
                System.addTask()
            case 2:
                System.removeTask()
            case 3:
                System.searchTask()
            case 4:
                System.showAllTask()
            case 5:
                System.clearLog()
            case 6:
                System.clearTask()
            case 7:
                print("Session Ended Sucessfully.")
                break
            case -1:
                pass
            case _:
                print("Choose valid value !!!")

initiate()
