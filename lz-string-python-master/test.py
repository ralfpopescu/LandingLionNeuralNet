"""
Copyright © 2014 Eduard Tomasek <???>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
"""

import json
import lzstring
import pprint


if __name__ == '__main__':
    x = lzstring.LZString()

    s = 'Žluťoučký kůň úpěl ďábelské ódy!'

    # generated with original js lib
    jsLzStringBase64 = 'r6ABsK6KaAD2aLCADWBfgBPQ9oCAlAZAvgDobEARlB4QAEOAjAUxAGd4BL5AZ4BMBPAQiAAA'
    jsLzStringBase64Json = 'N4Ig5gNg9gzjCGAnAniAXKALgS0xApuiPgB7wC2ADgQASSwIogA0IA4tHACLYBu6WXASIBlFu04wAMthiYBEhgFEAdpiYYQASS6i2AWSniRURJgCCMPYfEcGAFXyJyozPBUATJB5pt8Kp3gIbAAvfB99JABrAFdKGil3MBj4MEJWcwBjRCgVZBc0EBEDIwyAIzLEfH5CrREAeRoADiaAdgBONABGdqaANltJLnwAMwVKJHgicxpyfDcAWnJouJoIJJS05hoYmHCaTCgabPx4THxZlfj1lWTU/BgaGBjMgAsaeEeuKEyAISgoFEAHSDBgifD4cwQGBQdAAbXYNlYAA0bABdAC+rDscHBhEKy0QsUoIAxZLJQAAA=='

    print('String for encode: ' + s)
    print()

    print('Compress to base64:')
    base2 = x.compressToBase64(s)
    print('result:    ' + base2)
    print('result js: ' + jsLzStringBase64)
    print('equals:    ' + str(base2 == jsLzStringBase64))

    print()

    print('Decompress from base64:')
    print('result:         ' + x.decompresFromBase64(base2))
    print('result from js: ' + x.decompresFromBase64(jsLzStringBase64))

    print()

    jsonString = '{"glossary":{"title":"example glossary","GlossDiv":{"title":"S","GlossList":{"GlossEntry":{"ID":"SGML","SortAs":"SGML","GlossTerm":"Standard Generalized Markup Language","Acronym":"SGML","Abbrev":"ISO 8879:1986","GlossDef":{"para":"A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso":["GML","XML"]},"GlossSee":"markup"}}}}}'

    print('Compress json to base64:')
    jresult = x.compressToBase64(jsonString)
    print('result:    ' + jresult)
    print()
    print('result js: ' + jsLzStringBase64Json)
    print()
    print('equals: ' + str(jresult == jsLzStringBase64Json))

    print()

    print('Decompress json from base64:')
    pprint.pprint(json.loads(x.decompresFromBase64(jsLzStringBase64Json)))
