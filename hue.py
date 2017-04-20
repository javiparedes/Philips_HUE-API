#!/usr/bin/python

# Copyright (C) 2017 Javier Paredes javi.paredes@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import requests

class Hue(object):

	def __init__(self,ip,token):
		self.ip=ip
		self.token=token
		self.url="http://%s/api/%s/" % (self.ip,self.token)

	def get_all_lights(self):
		r=requests.get(self.url+"lights")
		return r.json()

	def get_new_lights(self):
		r=requests.get(self.url+"lights/new")
		return r.json()

	def search_new_lights(self,deviceid):
		parameters={}
		parameters["deviceid"]=deviceid
		r=requests.post(self.url+"lights",json=parameters)
		return r.json()

	def get_light_attributes_state(self,light_id):
		r=requests.get(self.url+"lights/"+light_id)
		return r.json()

	def set_light_attributes(self,light_id,name):
		parameters={}
		parameters["name"]=name
		r=requests.post(self.url+"lights/"+light_id,json=parameters)
		return r.json()

	def set_light_state(self,light_id,on="",bri="",hue="",sat="",xy="",ct="",alert=0,effect=0,transitiontime="",bri_inc="",sat_inc="",hue_inc="",ct_inc="",xy_inc=""):
		parameters={}
		if type(on) is bool:
			parameters["on"]=on
		if type(bri) is int and bri>0 and bri<255:
			parameters["bri"]=bri
		if type(hue) is int and hue>-1 and hue<65536:
			parameters["hue"]=hue
		if type(sat) is int and sat>-1 and sat<255:
			parameters["sat"]=sat
		if type(xy) is list and len(xy)==2 and type(xy[0]) is float and xy[0]>=0 and xy[0]<=1 and type(xy[1]) is float and xy[1]>=0 and xy[1]<=0:
			parameters["xy"]=xy
		if type(ct) is int and ct>152 and ct<501:
			parameters["ct"]=ct
		if type(alert) is str and alert in ["none","select","lselect"]:
			parameters["alert"]=alert
		if type(effect) is str and effect in ["none","colorloop"]:
			parameters["effect"]=effect
		if type(transitiontime) is int and transitiontime>-1:
			parameters["transitiontime"]=transitiontime
		if type(bri_inc) is int and bri_inc>-255 and bri_inc<255:
			parameters["bri_inc"]=bri_inc
		if type(hue_inc) is int and hue_inc>-65535 and hue_inc<65535:
			parameters["hue_inc"]=hue_inc
		if type(ct_inc) is int and ct_inc>-65535 and ct_inc<65535:
			parameters["ct_inc"]=ct_inc
		if type(xy_inc) is list and len(xy_inc)==2 and type(xy_inc[0]) is float and xy_inc[0]>=-1 and xy_inc[0]<=1 and type(xy_inc[1]) is float and xy_inc[1]>=0 and xy_inc[1]<=-1:
			parameters["xy"]=xy
		r=requests.put(self.url+"lights/"+light_id+"/state",json=parameters)
		return r.json()

	def delete_light(self,light_id):
		r=requests.delete(self.url+"lights/"+light_id)
		return r.json()
