from tinydb import TinyDB, Query
import random

db = TinyDB('data/monster_data_lvl_one.json')
App = Query()

db.insert({
  'name': 'Goblin',
  'health': 12,
  'weapon': 1,
  'strength': 8,
  'dexterity': 8,
  'intelligence': 8,
  'wisdom': 8,
  'armor-class': 8,
  'id': 1
})

db.insert({
  'name': 'Skeleton',
  'health': 15,
  'weapon': 1,
  'strength': 7,
  'dexterity': 10,
  'intelligence': 8,
  'wisdom': 8,
  'armor-class': 8,
  'id': 2
})

db.insert({
  'name': 'Zombie',
  'health': 15,
  'weapon': 0,
  'strength': 10,
  'dexterity': 10,
  'intelligence': 8,
  'wisdom': 8,
  'armor-class': 8,
  'id': 3
})

db.insert({
  'name': 'Gravemonster',
  'health': 15,
  'weapon': 1,
  'strength': 10,
  'dexterity': 10,
  'intelligence': 8,
  'wisdom': 8,
  'armor-class': 8,
  'id': 4
})
