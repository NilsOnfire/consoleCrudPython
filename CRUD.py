def listCourses(courses):
    print("\n---CURSOS---\n")
    count = 1
    for course in courses:
        data = "{0}.\tID: {1}\tName: {2} ({3} Credits)"
        print(data.format(count, course[0], course[1], course[2]))

        count += 1
    print('\n')


def getDataToInsert():
    name = input("Enter the name of course: ")
    credit = int(input("Enter credit amount: "))
    course = (name, credit)

    return course

def getDataUpdate(courses):
    listCourses(courses)
       
    existcode = False
    codUpdate = int(input("Enter the ID of row to update:  "))
 
    for course in courses:

        if course[0] == codUpdate:

            existcode = True
            break
    if  existcode:
        name = input("Enter the new name of course: ")
        credit = int(input("Enter the new credit amount: "))
        course = (codUpdate,name, credit)
    else:
        course = None
    return course
    
    

def getCodeDelete(courses):
    listCourses(courses)
    existcode = False
    codDelete = int(input("Enter an ID: "))
 
    for course in courses:

        if course[0] == codDelete:

            existcode = True
            break
    if not existcode:
        codDelete = ''

    return codDelete
