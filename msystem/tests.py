from django.test import TestCase
from MSystem.views import MainPage
from MSystem.models import Member, 



class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		resp =self.client.post('/', data= {
		'Name': 'juan j',
		'age' :'40',
		'address' : 'san antonio',
		'munc' : 'san antonio',
		'pro' : 'san antonio',
		'zip' : 'san antonio',
		'dswd' : '0011',
		})
		self.assertEqual(Member.objects.count(), 1)
		Mem = Member.objects.first()
		self.assertEqual(Mem.Name , 'juan j')
		self.assertEqual(Mem.Age , '40')
		self.assertEqual(Mem.Brgy , 'san antonio')
		self.assertEqual(Mem.Municipality , 'san antonio')
		self.assertEqual(Mem.Province, 'san antonio')
		self.assertEqual(Mem.ZipCode , 'san antonio')
		self.assertEqual(Mem.Dswd , '0011')


	def test_redirect_POST(self):
		response = self.client.post('/', data={ 
		'Name': 'juan j',
		'age' :'40',
		'address' : 'san antonio',
		'munc' : 'san antonio',
		'pro' : 'san antonio',
		'zip' : 'san antonio',
		'dswd' : '0011',
        })
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Member.objects.count(), 0)


class ORMTest(TestCase):
 	def test_saving_retrieving_list(self):
 		list1 = Member()
 		list1.Name = 'juan j'
 		list1.Age = '40'
 		list1.Brgy = '40'
 		list1.Municipality = '40'
 		list1.Province = '40'
 		list1.ZipCode = '40'
 		list1.Dswd ='0011'
 		list1.save()

 		list2 = Member()
 		list2.Name = 'juan j'
 		list2.Age = '40'
 		list2.Brgy = '40'
 		list2.Municipality = '40'
 		list2.Province = '40'
 		list2.ZipCode = '40'
 		list2.Dswd ='0011'
 		list2.save()

 		mem = Member.objects.all()
 		self.assertEqual(mem.count(), 2)
 		mem1 = mem[0
] 		mem2 = mem[1]


 		self.assertEqual(mem2.Name , 'juan j')
		self.assertEqual(mem2.Age , '40')
		self.assertEqual(mem2.Brgy , 'san antonio')
		self.assertEqual(mem2.Municipality , 'san antonio')
		self.assertEqual(mem2.Province, 'san antonio')
		self.assertEqual(mem2.ZipCode , 'san antonio')
		self.assertEqual(mem2.Dswd , '0011')

 		self.assertEqual(mem1.Name , 'juan j')
		self.assertEqual(mem1.Age , '40')
		self.assertEqual(mem1.Brgy , 'san antonio')
		self.assertEqual(mem1.Municipality , 'san antonio')
		self.assertEqual(mem1.Province, 'san antonio')
		self.assertEqual(mem1.ZipCode , 'san antonio')
		self.assertEqual(mem1.Dswd , '0011')



	def test_template_displays_list(self):
 		Member.objects.create(Name='juan j',
 			Age= request.POST['age'],
            Brgy= request.POST['address'],
            Municipality= request.POST['munc'],
            Province= request.POST['pro'],
            ZipCode= request.POST['zip'],
            Dswd= request.POST['dswd'],)
 		Member.objects.create(Name='john b',
 			Age= request.POST['age'],
            Brgy= request.POST['address'],
            Municipality= request.POST['munc'],
            Province= request.POST['pro'],
            ZipCode= request.POST['zip'],
            Dswd= request.POST['dswd'],)
 		response = self.client.get('/')
 		self.assertIn('1: juan j san antonio 40 0011', response.content.decode())
 		self.assertIn('2: john b san carlos 30 0022', response.content.decode())

'''class HomePageTest(TestCase):

	def test_mainpage_as_seen_client(self):
		resp = self.client.get('/')
		self.assertTemplateUsed(resp, 'mainpage.html')
	
	def test_responding_post_request(self):
		resp = self.client.post('/', data={'Name' :'Name'})
		self.assertIn('Name', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'address' :'Address'})
		self.assertIn('Address', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'age' :'Age'})
		self.assertIn('Age', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'dswd' :'Dswd'})
		self.assertIn('dswd', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')

		resp = self.client.post('/', data={'member' :'Member'})
		self.assertIn('Member', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')'''


          
     




'''class HomePageTest(TestCase):

	def test_mainpage_as_seen_client(self):
		resp = self.client.get('/')
		self.assertTemplateUsed(resp, 'mainpage.html')
	
	def test_responding_post_request(self):
		resp = self.client.post('/', data={'Name' :'Name'})
		self.assertIn('Name', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'address' :'Address'})
		self.assertIn('Address', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'age' :'Age'})
		self.assertIn('Age', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')
		
		resp = self.client.post('/', data={'dswd' :'Dswd'})
		self.assertIn('dswd', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')

		resp = self.client.post('/', data={'member' :'Member'})
		self.assertIn('Member', resp.content.decode())
		self.assertTemplateUsed(resp, 'mainpage.html')'''


          
     



