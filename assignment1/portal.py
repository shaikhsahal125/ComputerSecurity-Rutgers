#! /usr/bin/env python3

import sys
import os
import json

class Portal:
    """ # AddUser Functionality
    * Loads the existing data into a dictionary from a file to check if user already exist
    * if the use is unique, add user into a dictionary with its password and store back to the file
    * if user is added it prints SUCCESS otherise ERROR
    """
    def addUser(self, user, password):
        # print('Checkpost 1')
        if not os.path.exists('./portal_data/accounts.txt'):
           # print('Checkpost 2')
            with open('./portal_data/accounts.txt', 'w') as json_file:
              #  print('Checkpost 3')
                users = {}
                users[user] = password
                json.dump(users, json_file)
                json_file.close()
        else:
            # print('Checkpost 4')
            with open('./portal_data/accounts.txt', 'r') as json_file:
                # print('Checkpost 5')
                users = json.load(json_file)
                json_file.close()

            if user in users:
                print("Error: user exists")
                return

            users[user] = password
            with open('./portal_data/accounts.txt', 'w') as json_file:
                json.dump(users, json_file)
                json_file.close()

        print('Success')


    """ # Authenticate Functionality
    * load existing data into dictionary from a file 
    * Check if the user exist and its password
    * if the authentication fails, it prints ERROR otherwise SUCCESS
    """
    def authenticate(self, user, password):
        if not os.path.exists('./portal_data/accounts.txt'):
            print('Error: no such user')
            return
        else:
            with open('./portal_data/accounts.txt', 'r') as json_file:
                users = json.load(json_file)
                if user not in users:
                    print('Error: no such user')
                else:
                    if users[user] == password:
                        print('Success')
                    else:
                        print('Error: bad password')
                json_file.close()

                
    """ # Set Domain Functionality 
    * loads data into dictionary an from files
    * Check users: if they dont exists, print ERROR
    * it stores the data into two files for better access
       * 1.>  {domain_name : [user1, user2, ....]}
       * 2.>  {user_name : [domain1, domain2, ...]}
    * Prints success after adding the data 
    """
    def setDomain(self, user, domain_name):
        if not os.path.exists('./portal_data/accounts.txt'):
            print('Error: no such user')
            return
        else:
            with open('./portal_data/accounts.txt', 'r') as json_file:
                users = json.load(json_file)
                json_file.close()

            if user not in users:
                print('Error: no such user')
                return

            if not os.path.exists('./portal_data/domains.txt'):
                with open('./portal_data/domains.txt', 'w') as json_file:
                    domains = {}
                    domains[domain_name] = [user]
                    json.dump(domains, json_file)
                    json_file.close()
            else:
                with open('./portal_data/domains.txt', 'r') as json_file:
                    domains = json.load(json_file)
                    json_file.close()

                if domain_name in domains:
                    if user not in domains[domain_name]:
                        domains[domain_name].append(user)
                    else:
                        print('Success') # make sure to check it
                        return
                else:
                    domains[domain_name] = [user]

                with open('./portal_data/domains.txt', 'w') as json_file:
                    json.dump(domains, json_file)
                    json_file.close()

            print('Success')


            if os.path.exists('./portal_data/user_domain.txt'):
                with open('./portal_data/user_domain.txt', 'r') as f:
                    user_domain = json.load(f)
                    f.close()

                if user in user_domain:
                    if domain_name not in user_domain[user]:
                        user_domain[user].append(domain_name)
                else:
                    user_domain[user] = [domain_name]

                with open('./portal_data/user_domain.txt', 'w') as f:
                    json.dump(user_domain, f)
                    f.close()
            else:
                user_domain = {}
                user_domain[user] = [domain_name]

                with open('./portal_data/user_domain.txt', 'w') as json_file:
                    json.dump(user_domain, json_file)
                    json_file.close()


    """ # Domain Info
    * loads the data into dictionary from file 
      * Example of dictionary {domain_name:[user1, user2, .....]}
    * Check if domain_name exist in the dictionary and print the entire list of users.
    """
    def domainInfo(self, domain_name):
        if not os.path.exists('./portal_data/domains.txt'):
            pass
        else:
            with open('./portal_data/domains.txt', 'r') as json_file:
                domains = json.load(json_file)
                if domain_name in domains:
                    for user in domains[domain_name]:
                        print(user)
                json_file.close()


    """ # Set Type Functionality
    * loads data into dictionary an from files
    * Check users: if they dont exists, print ERROR
    * it stores the data into two files for better access
       * 1.>  {type_name : [object1, object2, ....]}                                                  
       * 2.>  {object_name : [type1, type2, ...]}
    * Prints success after adding the data
    """
    def setType(self, object_name, type_name):
        if not os.path.exists('./portal_data/types.txt'):
            with open('./portal_data/types.txt', 'w') as json_file:
                type_store = {}
                type_store[type_name] = [object_name]
                json.dump(type_store, json_file)
                json_file.close()
        else:
            with open('./portal_data/types.txt', 'r') as json_file:
                type_store = json.load(json_file)
                json_file.close()

            if type_name in type_store:
                if object_name not in type_store[type_name]:
                    type_store[type_name].append(object_name)
                else:
                    print('Success') # might remove depending on prof.
                    return
            else:
                type_store[type_name] = [object_name]

            with open('./portal_data/types.txt', 'w') as json_file:
                json.dump(type_store, json_file)
                json_file.close()

        print('Success')

        if os.path.exists('./portal_data/object_type.txt'):
            # print('check point 1')
            with open('./portal_data/object_type.txt', 'r') as json_file:
                # print("check point 2")
                object_type = json.load(json_file)
                json_file.close()

            if object_name in object_type:
                # print("check point 3")
                if type_name not in object_type[object_name]:
                    object_type[object_name].append(type_name)
            else:
                # print("check point 4")
                object_type[object_name] = [type_name]

            with open('./portal_data/object_type.txt', 'w') as json_file:
                # print("check point 5")
                json.dump(object_type, json_file)
                json_file.close()
        else:
            object_type = {}
            object_type[object_name] = [type_name]

            with open('./portal_data/object_type.txt', 'w') as json_file:
                json.dump(object_type, json_file)
                json_file.close()

                
    """ # Type Info
    * loads the data into dictionary from file
      * Example of dictionary {type_name:[object1, object2, .....]}
    * Check if domain_name exist in the dictionary and print the entire list of users.
    """
    def typeInfo(self, type_name):
        if os.path.exists('./portal_data/types.txt'):
            with open('./portal_data/types.txt', 'r') as json_file:
                type_store = json.load(json_file)
                if type_name in type_store:
                    for object_name in type_store[type_name]:
                        print(object_name)
                json_file.close()


    """ # Add Access
    * Retrieve data from file into dictionary
    * Dictionary Formate {operation : {domain_name1 : [type1, type2], domain_name2 : [type3, type4]}}
    * adds the access permisstion into dictioanry and stores back to the file
    * Prints Success after adding the data
    """
    def addAccess(self, operation, domain_name, type_name):

        if not os.path.exists('./portal_data/access.txt'):
            with open('./portal_data/access.txt', 'w') as json_file:
                controll = {}
                controll[operation] = {domain_name:[type_name]}
                json.dump(controll, json_file)
                json_file.close()
        else:
            with open('./portal_data/access.txt', 'r') as json_file:
                controll = json.load(json_file)
                json_file.close()

            if operation in controll:
                if domain_name in controll[operation]:
                    if type_name not in controll[operation][domain_name]:
                        controll[operation][domain_name].append(type_name)
                else:
                    controll[operation][domain_name] = [type_name]
            else:
                controll[operation] = {domain_name:[type_name]}

            with open('./portal_data/access.txt', 'w') as json_file:
                json.dump(controll, json_file)
                json_file.close()

        print('Success')

        
    """ # Can Access
    * This method uses 4 different files to retrieve data into different dictionaries
    * Check if the user and object has a right to permission to use operation by accessing different dictionaries
    * it prints SUCCESS if it finds the right permission otherwise ACCESS DENIED.
    """
    def canAccess(self, operation, user, object_name):
        if os.path.exists('./portal_data/user_domain.txt'):
            with open('./portal_data/user_domain.txt', 'r') as f:
                user_domain = json.load(f)
                f.close()
        else:
            print('Error: access denied')
            return

        if os.path.exists('./portal_data/object_type.txt'):
            with open('./portal_data/object_type.txt', 'r') as f:
                obj_type = json.load(f)
                f.close()
        else:
            print('Error: access denied')
            return

        if os.path.exists('./portal_data/access.txt'):
            with open('./portal_data/access.txt', 'r') as f:
                access = json.load(f)
                f.close()
        else:
            print('Error: access denied')
            return

        present1, present2 = False, False
        d = set()
        if operation in access:
            if user in user_domain:
                for domain in user_domain[user]:
                    if domain in access[operation]:
                        d =  set(access[operation][domain])
                        present1 = True
                        break
            else:
                print('Error: domain not found for user')
                return

            if object_name in obj_type:
                for obj in obj_type[object_name]:
                    if obj in d:
                        present2 = True
                        break
            else:
                print('Error: access denied')
                return
        else:
            print("Error: access denied")
            return

        if present1 and present2:
            print('Success')
        else:
            print('Error: access denied')


# Main method 
def main():
    
    if not os.path.exists("./portal_data/"):
        os.mkdir("./portal_data/")

    portal = Portal()

    # check if there are at least two and maximum 5 arguments
    if len(sys.argv) < 2:
        print("Error: missing arguments")
        return

    if len(sys.argv) > 5:
        print("Error: too many arguments")
        return

    # conditions for AddUser operation
    if sys.argv[1].lower() == 'adduser':
        if len(sys.argv) != 4:
            print("Error: wrong arguments")
            return
        user = sys.argv[2]
        if user == "":
            print("Error: username missing")
            return
        password = sys.argv[3]
        portal.addUser(user, password)

    # conditions for Authenticate operation
    elif sys.argv[1].lower() == 'authenticate':
        if len(sys.argv) != 4:
            print("Error: wrong arguments")
            return
        user = sys.argv[2]
        password = sys.argv[3]
        portal.authenticate(user, password)

    # conditions for SetDomain operation
    elif sys.argv[1].lower() == 'setdomain':
        if len(sys.argv) != 4:
            print("Error: wrong arguments")
            return
        user = sys.argv[2]
        domain_name = sys.argv[3]
        if domain_name == "":
            print("Error: missing domain")
            return
        portal.setDomain(user, domain_name)

    # coditions for DomainInfo operation
    elif sys.argv[1].lower() == 'domaininfo':
        if len(sys.argv) != 3:
            print("Error: wrong arguments")
            return
        domain_name = sys.argv[2]
        if domain_name == "":
            print("Error: missing domain")
            return
        portal.domainInfo(domain_name)

    # conditions for SetType operation
    elif sys.argv[1].lower() == 'settype':
        if len(sys.argv) != 4:
            print("Error: wrong arguments")
            return
        object_name = sys.argv[2]
        type_name = sys.argv[3]
        portal.setType(object_name, type_name)

    # conditions for TypeInfo operation
    elif sys.argv[1].lower() == 'typeinfo':
        if len(sys.argv) != 3:
            print("Error: wrong arguments")
            return
        type_name = sys.argv[2]
        if type_name == "":
            print("Error: missing type_name")
            return
        portal.typeInfo(type_name)

    # conditions for AddAccess operation
    elif sys.argv[1].lower() == 'addaccess':
        if len(sys.argv) != 5:
            print("Error: wrong arguments")
            return
        operation = sys.argv[2]
        if operation == "":
            print('Error: missing operation')
            return

        domain_name = sys.argv[3]
        if domain_name == "":
            print('Error: missing domain')
            return

        type_name = sys.argv[4]
        if type_name == "":
            print('Error: missing type')
            return

        portal.addAccess(operation, domain_name, type_name)

    # conditions for CanAccess operation
    elif sys.argv[1].lower() == 'canaccess':
        if len(sys.argv) != 5:
            print("Error: wrong arguments")
            return
        operation = sys.argv[2]
        user = sys.argv[3]
        object_name = sys.argv[4]

        portal.canAccess(operation, user, object_name)

    else:
        print("Error: bad arguments")
        return
if __name__ == '__main__':
    main()
