from UserDAO import userDAO
from Logger_base import log
from Users import Users

option = None
while option != 5:
    print(
    '''
    OPTIONS:

    1. List Users
    2. Add Users
    3. Update Users
    4. Eliminated Users
    5. Exit Menu

    ''')

    option = int(input('Write the option(1-5):  '))

    if option == 1:
        usuarios = userDAO.select()
        for usuario in usuarios:
            log.info(usuario)
    elif option == 2:
        username_var = input('Write the Username: ')
        password_var = input('Write the Password: ')
        user1 = Users(username= username_var, password= password_var)
        users_inserted = userDAO.insert(user1)
        log.info(f'the succesfully inserted records were {users_inserted}\n')
    elif option == 3:
        
        username_var = input('Write the Username: ')
        password_var = input('Write the Password: ')
        id_user_var = int(input('Write id_user to update: '))
        user1 = Users(id_user=id_user_var, username= username_var, password= password_var )
        users_updates = userDAO.update(user1)
        log.info(f'The succesfully updated records were {users_updates}')
    elif option == 4:
        id_user_var = input('Write the User to deleted: ')
        user1= Users(id_user= id_user_var)
        users_deletes = userDAO.delete(user1)
        log.info(f'The succesfully deleted records were {users_deletes}')
else:
    log.info('You left the app...')