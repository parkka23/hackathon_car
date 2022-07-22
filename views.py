import json

class Car:
    FILE='jsondb/data.json'
    id=0
    

    # create
    def __init__(self, mark, model, year_of_manufacture, engine_capacity, color, body_type, mileage, price):
        self.mark=mark
        self.model=model
        self.year_of_manufacture=year_of_manufacture
        self.engine_capacity=round(engine_capacity,1)
        self.color=color
        self.body_type=body_type
        self.mileage=mileage
        self.price=round(price,2)
        self.likes=0
        self.comments=[]
        self.send_product_to_json()

    # auxiliary methods
    @classmethod
    def get_id(cls):
        cls.id+=1
        return cls.id

    @staticmethod
    def get_one_product(data,id):
        product= list(filter(lambda x:x['id']==id,data))
        if not product: 
            return 'Car record not found.'
        else: return product[0]

    @classmethod
    def send_data_to_json(cls,data):
        with open(cls.FILE,'w') as file:
            json.dump(data,file)

    def send_product_to_json(self):
        data=Car.get_data() # list of dictionaries
        product={
            'id':Car.get_id(),
            'mark':self.mark,
            'model':self.model,
            'year_of_manufacture':self.year_of_manufacture,
            'engine_capacity':self.engine_capacity,
            'color':self.color,
            'body_type':self.body_type,
            'mileage':self.mileage,
            'price':self.price,
            'likes':self.likes,
            'comments':self.comments
        }
        data.append(product)
        with open(Car.FILE,'w') as file:
            json.dump(data,file)
        response= {
            'Status':'201',
            'Message':'Successfully created.',
            'Product':product
        }
        print(response)

    # listing
    @classmethod
    def get_data(cls):
        with open(cls.FILE,'r') as file:
            return json.load(file)
    
    # retrieve
    @classmethod
    def retrieve_data(cls,id):
        data=Car.get_data()
        product=cls.get_one_product(data,id)
        return product

    # update
    @classmethod
    def update_data(cls,id,key,new_value):
        data=cls.get_data()
        product=cls.get_one_product(data,id)
        if type(product) != dict:
            return product
        index=data.index(product)
        data[index][key]=new_value
        cls.send_data_to_json(data)
        response= {
            'Status':'200',
            'msg':'Successfully updated.'
        }
        return response

    # delete
    @classmethod
    def delete_data(cls,id):
        data=cls.get_data()
        product=cls.get_one_product(data,id)
        if type(product) != dict:
            return product
        index=data.index(product)
        data.pop(index)
        cls.send_data_to_json(data)
        response= {
            'Status':'204',
            'msg':'Successfully deleted.'
        }
        return response

    # like
    @classmethod
    def like(cls,id):
        data=cls.get_data()
        product=cls.get_one_product(data,id)
        if type(product) != dict:
            return product
        index=data.index(product)
        data[index]['likes']+=1
        cls.send_data_to_json(data)
        response= {
            'Status':'200',
            'Message':'Successfully liked.',
        }
        return response

    # comment
    @classmethod
    def comment(cls,id,com):
        data=cls.get_data()
        product=cls.get_one_product(data,id)
        if type(product) != dict:
            return product
        index=data.index(product)
        data[index]['comments'].append(com)
        cls.send_data_to_json(data)
        response= {
            'Status':'200',
            'Message':'Successfully commented.',
        }
        return response
        
with open(Car.FILE,'w') as file:
    json.dump([],file)
