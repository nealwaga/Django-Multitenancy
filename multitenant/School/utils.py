from django.db import connection

# Create here
def hostname_from_the_request(request):  #takes the request and removes the ports and returns the bare URL
    return request.get_host().split(":")[0].lower() 

def tenant_db_from_the_request(request):  #calls the other two functions. By comparing the host’s URL from the request and the dictionary, it returns the name of the database that matches its tenant
    hostname = hostname_from_the_request(request)
    tenants_map = get_tenants_map()
    return tenants_map.get(hostname)

def get_tenants_map():  #returns a dictionary with the added tenant’s URLs as keys and their database names as the values
    return {
        "nairobi.school.local": "nairobi",
        "accra.school.local": "accra"
    }