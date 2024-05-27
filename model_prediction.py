# model_prediction.py

from common import *

def test_model_proc(fn):

    data_cat = ["Melanoma", "Basal Cell Carcinoma (BCC)"]

    # Define a function to perform skin disease prediction
    global id
    sqliteConnection = sqlite3.connect('evaluation1.db')
    cursor = sqliteConnection.cursor()
    
    # Model parameters and settings
    IMAGE_SIZE = 227
    LEARN_RATE = 1.0e-4
    CH=3
        
    # Model Architecture and Compilation
    if fn!="":
        # Load the pre-trained model
        model = load_model(r'C:\Users\User\OneDrive\Documents\Custom Office Templates\New folder\SkinDi 2.44\Models\best_model.h5')
        model2 = load_model('Image_classify1.h5')

        adam = Adam(learning_rate=LEARN_RATE, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0)
        model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])
        
        # Preprocess the selected image
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        img = img / 255.0
        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,CH)
        
        # Make a prediction
        prediction = model.predict(img)
        # print("Printing prediction :- ", prediction)
        # print("np.argmax(prediction) :- ", np.argmax(prediction))
        Skin_diseases=np.argmax(prediction)

        print("Model1 Result :- ", Skin_diseases)
        
        
        f1=open("id.txt","r")
        id=f1.read()
        
        
        
        f1.close()
        
        if Skin_diseases==0:
            Cd="Benign"
            # print("Benign")
            sqliteConnection = sqlite3.connect('evaluation1.db')
            # print("Connected to SQLite")
            
            # Fetch patient data from the database
            r_set = sqliteConnection.execute("select id from registration where id =" + str(id) +"");
            # print(r_set)
            i=0
            for row in r_set:
            #    print("id=",row[0],)
               b=row[0]
            #    print(b)
               r_set1 = sqliteConnection.execute("select * from registration where id =" + str(b) +"");
               
               # Write patient data to a report file
               with open(r"C:\Users\User\OneDrive\Documents\Custom Office Templates\New folder\Report.txt", 'w') as f:
                   for row in r_set1:
                       line = "ID:"+ "\t" + str(row[0])+","+ "\n"+ "Name:"+ "\t"+str(row[1])+ ","+ "\n"+ "Address:"+ "\t" + str(row[2])+"\n"+ " Result:-Benign"#,row[3],row[4],row[5],row[6]
                       f.write(line)
                    #    print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

        
        elif Skin_diseases==1:
            def preprocess_image(image_path):
                # img = Image.open(image_path)
                # img = img.resize((180, 180))  # Resize image to match the input size of the model
                image = tf.keras.utils.load_img(image_path, target_size=(180,180))
                img_arr = tf.keras.utils.array_to_img(image)
                img_bat=tf.expand_dims(img_arr,0)
                # img = np.array(img) / 255.0  # Normalize pixel values
                # img = img.reshape((1, 200, 200, 3))  # Reshape to match the input shape of the model
                return img_bat
            
            sample_image = preprocess_image(fn)
            predictions = model2.predict(sample_image)
            score = tf.nn.softmax(predictions)
            finalRes = data_cat[np.argmax(score)]

            print("Predictions :- ", predictions)
            print("Score :- ", score)
            print("FinalResult :- ", finalRes)

            # Cd = finalRes
            if predictions[0][0] > 0.5:
                Cd = "Basal Cell Carcinoma (BCC)"
                # print("Basal Cell Carcinoma (BCC)")
            else:
                Cd = "Melanoma"
                # print("Melanoma")

            # Cd="Malignant"
            # print("Malignant")
            sqliteConnection = sqlite3.connect('evaluation1.db')
            # print("Connected to SQLite")
            
            
            r_set = sqliteConnection.execute("select id from registration where id =" + str(id) +"");
            # print(r_set)
            i=0
            for row in r_set:
            #    print("stmt=",row[0],)
               b=row[0]
            #    print(b)
               r_set1 = sqliteConnection.execute("select * from registration where id =" + str(b) +"");
               
               # Write patient data to a report file
               with open(r"C:\Users\User\OneDrive\Documents\Custom Office Templates\New folder\Report.txt", 'w') as f:
                   for row in r_set1:
                       line = "ID:"+ "\t" + str(row[0]) +","+ "\n"+ "Name:"+ "\t"+str(row[1])+ ","+ "\n"+ "Address:"+ "\t" + str(row[2])+"\n"+" Result:-Malignant"#,row[3],row[4],row[5],row[6]
                       f.write(line)
                    #    print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                       
        A = Cd      
        return A
