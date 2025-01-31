# -*- coding: utf-8 -*-

from updater import Updater


class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.updater = Updater()

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                self.updater.update_sulfuras(item)
            elif item.name == "Aged Brie":
                self.updater.update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.updater.update_backstage_passes(item)
            elif item.name == "Conjured Mana Cake":
                self.updater.update_conjured(item)
            else:
                self.updater.update_default(item)



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
