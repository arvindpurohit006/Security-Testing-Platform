def select_attack():
    while True:
        try:
            print("1.prompt_injection \n2.jailbreak \n3.system_prompt_exposure \n4.sensitive_data_disclosure \n5.cross_user_data_access \n6.excessive_agency")
            user_select = int(input("Enter attack number: "))

            if user_select < 1 or user_select > 6:
                print("Invalid option. Please enter 1-6.\n")
                continue

            match user_select:
                case 1:
                    return "prompt_injection"
                case 2:
                    return "jailbreak"
                case 3:
                    return "system_prompt_exposure"
                case 4:
                    return "sensitive_data_disclosure"
                case 5:
                    return "cross_user_data_access"
                case 6:
                    return "excessive_agency"

        except ValueError:
            print("Invalid input. Enter numbers only.\n")


