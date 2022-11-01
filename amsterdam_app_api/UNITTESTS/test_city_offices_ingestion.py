
### These tests are copied from the original backend code base. Currently there is not
### Scraping, hence these tests are commented...


###def test_city_office_valid(self):
###    data = {
###        "identifier": "0000000000",
###        "title": "mock",
###        "contact": {
###            "Bellen": {
###                "html": "<div>mock</div>",
###                "text": "mock"
###            },
###            "Mailen": {
###                "html": "<div>mock</div>",
###                "text": "mock"
###            },
###            "Openingstijden": {
###                "html": "<div>mock</div>",
###                "text": "mock"
###            }
###        },
###        "images": {
###            "type": "",
###            "sources": {
###                "orig": {
###                    "url": "mock.jpg",
###                    "filename": "mock.jpg",
###                    "image_id": "00000000",
###                    "description": "mock"
###                }
###            }
###        },
###        "info": {
###            "html": "<div>mock</div>",
###            "text": "mock"
###        },
###        "address": {
###            "html": "<div>mock</div>",
###            "text": "mock"
###        }
###    }
###
###    result = self.client.post('/api/v1/ingest/cityoffice', data=data, headers=self.header,
###                              content_type='application/json')
###    db_objects = list(CityOffice.objects.filter(pk='0000000000').all())
###
###    self.assertEqual(result.status_code, 200)
###    self.assertEqual(result.data, {'status': True, 'result': True})
###    self.assertEqual(len(db_objects), 1)
###
###    # Test update same record
###    result = self.client.post('/api/v1/ingest/cityoffice', data=data, headers=self.header,
###                              content_type='application/json')
###    db_objects = list(CityOffice.objects.filter(pk='0000000000').all())
###
###    self.assertEqual(result.status_code, 200)
###    self.assertEqual(result.data, {'status': True, 'result': True})
###    self.assertEqual(len(db_objects), 1)
###
###
###def test_city_office_not_unique(self):
###    data = {'title': 'mock'}
###
###    result = self.client.post('/api/v1/ingest/cityoffice', data=data, headers=self.header,
###                              content_type='application/json')
###    db_objects = list(CityOffice.objects.all())
###
###    self.assertEqual(result.status_code, 200)
###    self.assertEqual(result.data, {'status': True, 'result': True})
###    self.assertEqual(len(db_objects), 1)
###
###    # Should fail, not unique
###    result = self.client.post('/api/v1/ingest/cityoffice', data=data, headers=self.header,
###                              content_type='application/json')
###    db_objects = list(CityOffice.objects.all())
###
###    self.assertEqual(result.status_code, 500)
###    self.assertEqual(result.data, {'status': False,
###                                   'result': 'duplicate key value violates unique constraint "amsterdam_app_api_cityoffice_pkey"\nDETAIL:  Key (identifier)=() already exists.\n'})
###    self.assertEqual(len(db_objects), 1)
###
###
###def test_city_offices_valid(self):
###    data = [{"url": "https://mock", "title": "mock", "identifier": "00000000"}]
###
###    result = self.client.post('/api/v1/ingest/cityoffices', data=data, headers=self.header,
###                              content_type='application/json')
###    db_objects = list(CityOffices.objects.all())
###
###    self.assertEqual(result.status_code, 200)
###    self.assertEqual(result.data, {'status': True, 'result': True})
###    self.assertEqual(len(db_objects), 1)
###
###    # 'Extra' call should still yield a single db record
###    data = [{"url": "https://mock", "title": "mock", "identifier": "00000000"},
###            {"url": "https://mock2", "title": "mock1", "identifier": "00000001"}]
###
###    result = self.client.post('/api/v1/ingest/cityoffices', data=data, headers=self.header,
###                              content_type='application/json')
###    db_objects = list(CityOffices.objects.all())
###
###    self.assertEqual(result.status_code, 200)
###    self.assertEqual(result.data, {'status': True, 'result': True})
###    self.assertEqual(len(db_objects), 1)
###
###
###def test_city_offices_invalid(self):
###    data = 'bogus'
###
###    result = self.client.post('/api/v1/ingest/cityoffices', data=data, headers=self.header,
###                              content_type='application/json')
###    db_objects = list(CityOffices.objects.all())
###
###    self.assertEqual(result.status_code, 500)
###    self.assertEqual(result.data, {'status': False, 'result': 'Caught error ingesting city offices'})
###    self.assertEqual(len(db_objects), 0)
###
###
###def test_city_contacts_valid(self):
###    data = [{"html": "<div>mock</div>", "text": "mock", "title": "mock"}]
###
###    result = self.client.post('/api/v1/ingest/citycontact', data=data, headers=self.header,
###                              content_type='application/json')
###    db_objects = list(CityContact.objects.all())
###
###    self.assertEqual(result.status_code, 200)
###    self.assertEqual(result.data, {'status': True, 'result': True})
###    self.assertEqual(len(db_objects), 1)
###
###
###def test_city_contacts_invalid(self):
###    data = 'bogus'
###
###    result = self.client.post('/api/v1/ingest/citycontact', data=data, headers=self.header,
###                              content_type='application/json')
###    db_objects = list(CityContact.objects.all())
###
###    self.assertEqual(result.status_code, 500)
###    self.assertEqual(result.data, {'status': False, 'result': 'Caught error ingesting city contacts'})
###    self.assertEqual(len(db_objects), 0)