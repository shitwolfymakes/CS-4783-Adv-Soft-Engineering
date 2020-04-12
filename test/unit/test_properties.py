import pytest
import requests
import json
from urllib3.exceptions import InsecureRequestWarning
from requests.auth import HTTPBasicAuth
import pymysql
import sys

#For unit testing, this uses a testing table to prevent changes to tbl_property

# delete anything that may be existing
conn = pymysql.connect(host='easel2.fulgentcorp.com', port=3306, user='xne693', passwd='v3FPwOMciKr1dIoHvKUJ', db='xne693')
cur = conn.cursor(pymysql.cursors.DictCursor)
sql = "DELETE FROM tbl_property"
cur.execute(sql)
conn.commit()

#reset counter for id at 1
conn = pymysql.connect(host='easel2.fulgentcorp.com', port=3306, user='xne693', passwd='v3FPwOMciKr1dIoHvKUJ', db='xne693')
cur = conn.cursor(pymysql.cursors.DictCursor)
sql = "ALTER TABLE tbl_property AUTO_INCREMENT = 1"
cur.execute(sql)
conn.commit()

# set up with one expected row
sql = "INSERT INTO tbl_property(ID, address, city, state, zip) VALUES(NULL, %s, %s, %s, %s)"
data = ("123 Valid Address", "Valid City", "ST", "12345")
conn = pymysql.connect(host='easel2.fulgentcorp.com', port=3306, user='xne693', passwd='v3FPwOMciKr1dIoHvKUJ', db='xne693')
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute(sql, data)
conn.commit()

# set up with second expected row
sql = "INSERT INTO tbl_property(ID, address, city, state, zip) VALUES(NULL, %s, %s, %s, %s)"
data = ("123 My Street", "San Antonio", "TX", "77777")
conn = pymysql.connect(host='easel2.fulgentcorp.com', port=3306, user='xne693', passwd='v3FPwOMciKr1dIoHvKUJ', db='xne693')
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute(sql, data)
conn.commit()


@pytest.fixture
def supply_url():
    return "https://cs47832.fulgentcorp.com:12137"

#test hello returns correct response code
def test_hello(supply_url):
    url = supply_url + "/hello"
    resp = requests.get(url, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text

#test hello returns correct response code
def test_add_property_get(supply_url):
    url = supply_url + "/properties"
    resp = requests.get(url, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text

#test post with correct data
def test_add_property_post(supply_url):
    url = supply_url + "/properties"
    payload = "{\"address\": \"1112 Testing St\", \"city\": \"Test City\", \"state\": \"ST\", \"zip\": \"11111\"}"
    headers = {
        'x-api-key': "cs4783FTW",
        'cache-control': "no-cache"
    }
    resp = requests.request("POST", url, data=payload, headers=headers, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text

#test post with bad address
def test_add_property_post_ba(supply_url):
    url = supply_url + "/properties"
    payload = "{\"address\": \"111 Testing Sttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt111 Testing SttttttttttttttttttttttttttttttttttttttTOOLONG\", \"city\": \"Test City\", \"state\": \"ST\", \"zip\": \"11111\"}"
    headers = {
        'x-api-key': "cs4783FTW",
        'cache-control': "no-cache"
    }
    resp = requests.request("POST", url, data=payload, headers=headers, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 400, resp.text
    #assert j['error'] ==

#test post with bad city
def test_add_property_post_bc(supply_url):
    url = supply_url + "/properties"
    payload = "{\"address\": \"111 Testing St\", \"city\": \"Test CityBADTest CityBADTest CityBADTest CityBADTest CityBADTest CityBAD\", \"state\": \"ST\", \"zip\": \"11111\"}"
    headers = {
        'x-api-key': "cs4783FTW",
        'cache-control': "no-cache"
    }
    resp = requests.request("POST", url, data=payload, headers=headers, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 400, resp.text

#test post with bad state
def test_add_property_post_bs(supply_url):
    url = supply_url + "/properties"
    payload = "{\"address\": \"111 Testing St\", \"city\": \"Test City\", \"state\": \"S\", \"zip\": \"11111\"}"
    headers = {
        'x-api-key': "cs4783FTW",
        'cache-control': "no-cache"
    }
    resp = requests.request("POST", url, data=payload, headers=headers, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 400, resp.text

#test post with bad zipcode
def test_add_property_post_bz(supply_url):
    url = supply_url + "/properties"
    payload = "{\"address\": \"111 Testing St\", \"city\": \"Test City\", \"state\": \"ST\", \"zip\": \"111\"}"
    headers = {
        'x-api-key': "cs4783FTW",
        'cache-control': "no-cache"
    }
    resp = requests.request("POST", url, data=payload, headers=headers, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 400, resp.text

#test post with incorrect api key
def test_add_property_post_badkey(supply_url):
    url = supply_url + "/properties"
    payload = "{\"address\": \"111 Testing St\", \"city\": \"Test City\", \"state\": \"ST\", \"zip\": \"11111\"}"
    headers = {
        'x-api-key': "idk",
        'cache-control': "no-cache"
    }
    resp = requests.request("POST", url, data=payload, headers=headers, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 401, resp.text

#test by id: get with correct data
def test_id_property_get(supply_url):
    id = 1
    url = supply_url + "/properties/" + str(id)
    resp = requests.request("GET", url, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text

#test by id: get with incorrect correct data
def test_id_property_get_dne(supply_url):
    id = 100
    url = supply_url + "/properties/" + str(id)
    resp = requests.request("GET", url, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 404, resp.text

#test by id: get with non-int id
def test_id_property_get_nonint(supply_url):
    id = "one"
    url = supply_url + "/properties/" + str(id)
    resp = requests.request("GET", url, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 400, resp.text

#test by id: post with incorrect api key
def test_id_add_property_delete_badkey(supply_url):
    id = 2
    url = supply_url + "/properties/" + str(id)
    headers = {
        'x-api-key': "idk",
        'cache-control': "no-cache"
    }
    resp = requests.request("DELETE", url, headers=headers, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 401, resp.text

#test by id: post with correct api key
def test_id_add_property_delete_goodkey(supply_url):
    id = 2
    url = supply_url + "/properties/" + str(id)
    headers = {
        'x-api-key': "cs4783FTW",
        'cache-control': "no-cache"
    }
    resp = requests.request("DELETE", url, headers=headers, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text

#test by id: post with non existing id
def test_id_add_property_delete_notexisting(supply_url):
    id = 2
    url = supply_url + "/properties/" + str(id)
    headers = {
        'x-api-key': "cs4783FTW",
        'cache-control': "no-cache"
    }
    resp = requests.request("DELETE", url, headers=headers, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 404, resp.text

#test by id: post with non int id
def test_id_add_property_delete_nonint(supply_url):
    id = "one"
    url = supply_url + "/properties/" + str(id)
    headers = {
        'x-api-key': "cs4783FTW",
        'cache-control': "no-cache"
    }
    resp = requests.request("DELETE", url, headers=headers, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 400, resp.text

#test put with good info
def test_id_property_put(supply_url):
    id = 3
    url = supply_url + "/properties/" + str(id)
    payload = "{\"address\": \"22 Testing St\", \"city\": \"San Diego\"}"
    headers = {
        'x-api-key': "cs4783FTW",
        'cache-control': "no-cache"
    }
    resp = requests.request("PUT", url, data=payload, headers=headers, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text

#test put with incorrect api key
def test_id_property_put_badkey(supply_url):
    id = 3
    url = supply_url + "/properties/" + str(id)
    payload = "{\"address\": \"22 Testing St\", \"city\": \"San Diego\"}"
    headers = {
        'x-api-key': "idk",
        'cache-control': "no-cache"
    }
    resp = requests.request("PUT", url, data=payload, headers=headers, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 401, resp.text

#test put with non existing id
def test_id_property_put_dne(supply_url):
    id = 2
    url = supply_url + "/properties/" + str(id)
    payload = "{\"address\": \"22 Testing St\", \"city\": \"San Diego\"}"
    headers = {
        'x-api-key': "cs4783FTW",
        'cache-control': "no-cache"
    }
    resp = requests.request("PUT", url, data=payload, headers=headers, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 404, resp.text

# test put with non int id
def test_id_property_put_nonint(supply_url):
    id = "one"
    url = supply_url + "/properties/" + str(id)
    payload = "{\"address\": \"22 Testing St\", \"city\": \"San Diego\"}"
    headers = {
        'x-api-key': "cs4783FTW",
        'cache-control': "no-cache"
    }
    resp = requests.request("PUT", url, data=payload, headers=headers, verify=False)
    j = json.loads(resp.text)
    assert resp.status_code == 400, resp.text