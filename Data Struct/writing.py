def clenanFile(currentMem, exMem):
    with open("currentMem","r+") as memfile:
        with open("exMem", "a+") as exfile:

            lines = memfile.readlines()

            header = lines[0]
            members = lines[1:]

            active = [header]
            inactive = []

            for member in members:
                if 'no' in member:
                    inactive.append(member)
                else:
                    active.append(member)

            
            memfile.seek(0)
            memfile.writelines(active)
            memfile.truncate()

            exfile.writelines(inactive)
