import mysql.connector
import json

from tqdm import tqdm

db = mysql.connector.connect(user="root", password="misfanatik", database="glove")
cursor = db.cursor()

#pbar = tqdm(total=325209)
pbar = tqdm(total=331285)
with open("./GloVe-1.2/vectors.txt") as f:
    try:
        for line in f:
            wv = line.split('\n')
            wv = wv[0].split()
            key = wv[0]
            vec = wv[1:]
            json_vec = json.JSONEncoder().encode(vec)
            #decoded_vec = json.JSONDecoder().decode(json_vec)
            #vec_d = np.asarray(decoded_vec, dtype=np.float32)

            sql = "insert into term (term, vec) values('"+ key +"', '" + json_vec + "')"
            cursor.execute(sql)

            pbar.update(1)

        pbar.close()
        print "DB COMMIT..."
        db.commit()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print sql
        db.rollback()

print "SUCCESS"
db.close()
cursor.close()
