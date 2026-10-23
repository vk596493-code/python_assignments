language = input("Enter language: ").lower()

match language:
    case "python":
        print("Python is easy to learn")
    case "java":
        print("Java is platform independent")
    case "c":
        print("C is a procedural language")
    case _:
        print("Language not available")