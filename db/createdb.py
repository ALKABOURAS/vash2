import sqlite3
import os
from pprint import pprint
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path + '/initial_db.db')
c = conn.cursor()
c.execute("""DROP TABLE IF EXISTS 'PICTURE';""")
c.execute("""DROP TABLE IF EXISTS 'PICTURE_APP';""")
c.execute("""
CREATE TABLE 'PICTURE' (
    'Pic_ID' INTEGER PRIMARY KEY AUTOINCREMENT,
    'Pic_Name' TEXT NOT NULL,
    'Pic_Path' TEXT NOT NULL);
""")
c.execute("""
CREATE TABLE 'PICTURE_APP' (
    'Pic_ID' INTEGER NOT NULL,
    'App_ID' TEXT NOT NULL,
    FOREIGN KEY('Pic_ID') REFERENCES PICTURE(Pic_ID) ON DELETE CASCADE,
    FOREIGN KEY('App_ID') REFERENCES APP(ID) ON DELETE CASCADE
    );
    """)
picname= ['android','boat','camera','phone','note']
picpath = ['C:\\android.jpg','C:\\boat.jpg','C:\\camera.jpg','C:\\phone.jpg','C:\\note.jpg']
for i in range(0,5):
    c.execute("""INSERT INTO PICTURE (Pic_Name,Pic_Path) VALUES (?,?)""",(picname[i],picpath[i]))
picid = [1,1,4,3,4,1,3,5]
appid=['com.facebook.katana','com.viber.voip','com.whatsapp','com.instagram.android','com.facebook.talk','com.zhiliaoapp.musically','com.viki.android','com.spotify.music']
for i in range(0,8):
    c.execute("""INSERT INTO PICTURE_APP (Pic_ID,App_ID) VALUES (?,?)""",(picid[i],appid[i]))
conn.commit()

# 1. Print all from rating where appid = 'com.facebook.katana'
print('1. Print all from rating where appid = com.facebook.katana')
c.execute("""SELECT * FROM RATING WHERE App_ID = 'com.facebook.katana'""")
print(c.fetchall())
print('\n')

# 2. Print all apps where id has the word 'android' or belong in the category 'COMMUNICATION'
print('2. Print all apps where id has the word android or belong in the category COMMUNICATION')
c.execute("""SELECT * FROM APP WHERE ID LIKE '%android%' OR Category_Name = 'COMMUNICATION'""")
print(c.fetchall())
print('\n')

# 3. For each rating print the app name, the rating value, the rating date by descending order of rating value
print('3. For each rating print the app name, the rating value, the rating date by descending order of rating value')
c.execute("""SELECT APP.Name, RATING.Value, RATING.Date FROM APP INNER JOIN RATING ON APP.ID = RATING.App_ID ORDER BY RATING.Value DESC""")
print(c.fetchall())
print('\n')

# 4. Print the app name, the rating value, the rating date by ascending order of rating value where the category name is 'SOCIAL'
print('4. Print the app name, the rating value, the rating date by ascending order of rating value where the category name is SOCIAL')
c.execute("""SELECT APP.Name, RATING.Value, RATING.Date FROM APP INNER JOIN RATING ON APP.ID = RATING.App_ID WHERE APP.Category_Name = 'SOCIAL' ORDER BY RATING.Value ASC""")
print(c.fetchall())
print('\n')

# 5. Print the developer name and the email of the developer where the developer email has the word 'android' as 'ΟΝΟΜΑ', 'email'
print('5. Print the developer name and the email of the developer where the developer email has the word android as ΟΝΟΜΑ, email')
c.execute("""SELECT Name as 'ΟΝΟΜΑ', Email as 'email' FROM DEVELOPER WHERE Email LIKE '%android%'""")
print(c.fetchall())
print('\n')

# 6. Print the sum of apps where developer name is 'Meta Platforms Inc.' as 'Πλήθος Εφαρμογών'
print('6. Print the sum of apps where developer name is Meta Platforms Inc. as Πλήθος Εφαρμογών')
c.execute("""SELECT COUNT(*) as 'Πλήθος Εφαρμογών' FROM APP INNER JOIN DEVELOPER ON APP.Developer_ID = DEVELOPER.Dev_ID WHERE DEVELOPER.Name = 'Meta Platforms, Inc.'""")
print(c.fetchall())
print('\n')

# 7. Print pic_id and the sum of apps for each pic_id as 'Κωδικός Εικόνας', 'Πλήθος Εφαρμογών'
print('7. Print pic_id and the sum of apps for each pic_id as Κωδικός Εικόνας, Πλήθος Εφαρμογών')
c.execute("""SELECT PICTURE.Pic_ID as 'Κωδικός Εικόνας', COUNT(*) as 'Πλήθος Εφαρμογών' FROM PICTURE INNER JOIN PICTURE_APP ON PICTURE.Pic_ID = PICTURE_APP.Pic_ID GROUP BY PICTURE.Pic_ID""")
print(c.fetchall())
print('\n')

# 8. Print pic name and the sum of apps for each pic name as 'Όνομα Εικόνας', 'Πλήθος Εφαρμογών'
print('8. Print pic name and the sum of apps for each pic name as Όνομα Εικόνας, Πλήθος Εφαρμογών')
c.execute("""SELECT PICTURE.Pic_Name as 'Όνομα Εικόνας', COUNT(*) as 'Πλήθος Εφαρμογών' FROM PICTURE INNER JOIN PICTURE_APP ON PICTURE.Pic_ID = PICTURE_APP.Pic_ID GROUP BY PICTURE.Pic_Name""")
print(c.fetchall())
print('\n')

# 9. Print the average rating of the app where the app id is 'com.viki.android' rounded with 2 decimal digits as 'Μέση Βαθμολογία'
print('9. Print the average rating of the app where the app id is com.viki.android rounded with 2 decimal digits as Μέση Βαθμολογία')
c.execute("""SELECT ROUND(AVG(RATING.Value),2) as 'Μέση Βαθμολογία' FROM RATING INNER JOIN APP ON RATING.App_ID = APP.ID WHERE APP.ID = 'com.viki.android'""")
print(c.fetchall())
print('\n')

# 10. Print operating app id of apps that have operating_system both 'Android' and 'Windows'
print('10. Print operating app id of apps that have operating_system both Android and Windows')
c.execute("""SELECT App_ID FROM OPERATING WHERE Operating_System = 'Android' INTERSECT SELECT App_ID FROM OPERATING WHERE Operating_System = 'Windows'""")
print(c.fetchall())
print('\n')

# 11. Print all the pic names minus the pic names that are used
print('11. Print all the pic names minus the pic names that are used')
c.execute("""SELECT Pic_Name FROM PICTURE WHERE Pic_ID NOT IN (SELECT Pic_ID FROM PICTURE_APP)""")
print(c.fetchall())
print('\n')

# 12. Print app id and the rating value of the apps with the lowest rating values
print('12. Print app id and the rating value of the apps with the lowest rating values')
c.execute("""SELECT App_ID, Value FROM RATING WHERE Value = (SELECT MIN(Value) FROM RATING)""")
print(c.fetchall())
print('\n')


conn.close()