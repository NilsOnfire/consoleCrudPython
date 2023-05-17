from BD.conecction import DAO
import CRUD


def mainMenu():
    flag = True
    while flag:
        isCorrectOption = True
        while isCorrectOption:
            print(
                '''
|--------MENU---------|
 1-- Listar cursos.
 2-- Registrar curso.
 3-- Actualizar curso.
 4-- Eliminar curso.
 5-- Salir.
|---------------------|                
                '''
            )
            option = int(input("Select an option: "))
            if option < 1 or option > 5:
                isCorrectOption = False
                print("Incorrect option :(")
            elif option == 5:
                flag = False
                print("Closed system.")
            else:
                executeOption(option)


def executeOption(option):
    if option == 1:
        try:
            objDao = DAO()
            courses = objDao.listCourses()
     
            if len(courses)>0:
                CRUD.listCourses(courses)
            else:
                print("No se encontraron cursos")

        except:
            print("There was an error :(")
    elif option == 2:
       course = CRUD.getDataToInsert()
       try:
            objDao = DAO()
           
            objDao.createCourse(course) 
  
       except:
           print("Error")     
    elif option == 3:
        try:
            
            objDao = DAO()
            courses = objDao.listCourses()
            
            if len(courses)>0:
                course = CRUD.getDataUpdate(courses)
                if course:
                    objDao.updateCourse(course)      
                else:
                    print("No se encontraron cursos")   
     
            
        except:    
            print("Delete error")
    elif option == 4:
        
        try:
            
            objDao = DAO()
            courses = objDao.listCourses()
          
            if len(courses)>0:
                # CRUD.listCourses(courses)
                codCourse = CRUD.getCodeDelete(courses)
                if not(codCourse == ''):
                    objDao.deleteCourse(codCourse)
                else:
                    print("Codigo de curso no encontrado")    
            else:
                print("No se encontraron cursos")   
     
            
        except:    
            print("Delete error")
        
    else:
        print("Invalid option.")


mainMenu()
