class Updater:
    def __init__(self):
        pass

    def update_default(self, item):
        if(item.sell_in > 0):
            item.quality -= 1
        else:
            item.quality -= 2
        item.quality = max(0, item.quality)
        item.sell_in -= 1

    def update_sulfuras(self, item):
        pass

    def update_backstage_passes(self, item):
        if(item.sell_in <= 0):
            item.quality = 0
        elif(item.sell_in <= 5):
            item.quality += 3
        elif(item.sell_in <= 10):
            item.quality += 2
        else:
            item.quality += 1
        item.quality = min(50, item.quality)
        item.sell_in -= 1

    def update_aged_brie(self, item):
        if(item.sell_in > 0):
            item.quality += 1
        else:
            item.quality += 2
        item.quality = min(50, item.quality)
        item.sell_in -= 1

    def update_conjured(self, item):
        if(item.sell_in > 0):
            item.quality -= 2
        else:
            item.quality -= 4
        item.quality = max(0, item.quality)
        item.sell_in -= 1