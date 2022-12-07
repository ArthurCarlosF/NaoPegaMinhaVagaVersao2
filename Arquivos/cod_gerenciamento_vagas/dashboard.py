from tkinter import *
from PIL import Image, ImageTk
from paho.mqtt import client as mqtt_client
import json
from random import randint
 
# https://mntolia.com/10-free-public-private-mqtt-brokers-for-testing-prototyping/ 

broker = 'broker.hivemq.com'
port = 1883
topic = "api/teste/gcmo"
#topic_sub = "api/notification/37/#"
# generate client ID with pub prefix randomly
client_id = 'ID'+str(randint(0,1000))
#username = 'your username'
#password = 'your password'
deviceId = 'ID'+str(randint(0,1000))
 
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc==0:
            print("Conectado ao MQTT broker")
        else:
            print("Falha ao conectar, codigo de erro: %d", rc)
 
 
    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
 
def publish(client,status):
    # msg = f"messages: {msg_count}"
    msg = "{\"action\":\"command/insert\",\"deviceId\":\""+deviceId+"\",\"command\":{\"command\":\"LED_control\",\"parameters\":{\"led\":\""+status+"\"}}}"
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Mensamge `{msg}` enviada para o topico `{topic}`")
    else:
        print(f"Erro eu enviar mensagem para o topico {topic}")
 
 
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Recieved '{msg.payload.decode()}' from '{msg.topic}' topic")
        y = json.loads(msg.payload.decode())
        if y["action"] == "notification/insert" :
            vagas = [str(y["notification"]["parameters"]["vag"+str(i+1)]) for i in range(24)]
    
            vagas1_label.config(image= car if vagas[0] == "1" else ball)
            vagas2_label.config(image= car if vagas[1] == "1" else ball)
            vagas3_label.config(image= car if vagas[2] == "1" else ball)
            vagas4_label.config(image= car if vagas[3] == "1" else ball)
            vagas5_label.config(image= car if vagas[4] == "1" else ball)
            vagas6_label.config(image= car if vagas[5] == "1" else ball)
            vagas7_label.config(image= car if vagas[6] == "1" else ball)
            vagas8_label.config(image= car if vagas[7] == "1" else ball)
            vagas9_label.config(image= car if vagas[8] == "1" else ball)
            vagas10_label.config(image= car if vagas[9] == "1" else ball)
            vagas11_label.config(image= car if vagas[10] == "1" else ball)
            vagas12_label.config(image= car if vagas[11] == "1" else ball)
            vagas13_label.config(image= car if vagas[12] == "1" else ball)
            vagas14_label.config(image= car if vagas[13] == "1" else ball)
            vagas15_label.config(image= car if vagas[14] == "1" else ball)
            vagas16_label.config(image= car if vagas[15] == "1" else ball)
            vagas17_label.config(image= car if vagas[16] == "1" else ball)
            vagas18_label.config(image= car if vagas[17] == "1" else ball)
            vagas19_label.config(image= car if vagas[18] == "1" else ball)
            vagas20_label.config(image= car if vagas[19] == "1" else ball)
            vagas21_label.config(image= car if vagas[20] == "1" else ball)
            vagas22_label.config(image= car if vagas[21] == "1" else ball)
            vagas23_label.config(image= car if vagas[22] == "1" else ball)
            vagas24_label.config(image= car if vagas[23] == "1" else ball)

            qvagas_label.config(text = "VAGAS DISPONÍVEIS: "+ str(vagas.count("0")))
            qvagas_label.config(fg = "red" if str(vagas.count("0")) == "0" else "green")

    client.subscribe(topic)
    client.on_message = on_message
 
window = Tk()
window.title("MQTT Dashboard")
window.geometry('1312x586')
window.resizable(False,False)
window.configure(bg="white")
canvas = Canvas(window, bg="white", width=1312,height=586)
canvas.place(x=0,y=0)
image = Image.open("images/estacionamento.png")
image = image.resize((1312,586), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
canvas.create_image(0,0,anchor=NW,image=img)

# Define Our Images
image = Image.open("images/bola.png")
image = image.resize((62,44), Image.ANTIALIAS)
ball = ImageTk.PhotoImage(image)

image = Image.open("images/carro.png")
image = image.resize((62,138), Image.ANTIALIAS)
car = ImageTk.PhotoImage(image)


# Create Label
qvagas_label = Label(window,
                text = "VAGAS DISPONÍVEIS:",
                bg = '#D8D8D8',
                font = ("Segoe UI Black", 22))
                    
qvagas_label.place(x=450,y=300)

# Create Label
vagas1_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas1_label.place(x=48,y=95)

# Create Label
vagas2_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas2_label.place(x=128,y=95)

# Create Label
vagas3_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas3_label.place(x=208,y=95)

# Create Label
vagas4_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas4_label.place(x=288,y=95)

# Create Label
vagas5_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas5_label.place(x=366,y=95)

# Create Label
vagas6_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas6_label.place(x=444,y=95)

# Create Label
vagas7_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas7_label.place(x=524,y=95)

# Create Label
vagas8_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas8_label.place(x=604,y=95)

# Create Label
vagas9_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas9_label.place(x=684,y=95)

# Create Label
vagas10_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas10_label.place(x=762,y=95)

# Create Label
vagas11_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas11_label.place(x=882,y=95)

# Create Label
vagas12_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas12_label.place(x=1002,y=95)

# Create Label
vagas13_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas13_label.place(x=1082,y=95)

# Create Label
vagas14_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas14_label.place(x=1162,y=95)

# Create Label
vagas15_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas15_label.place(x=1242,y=95)

# Create Label
vagas16_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas16_label.place(x=48,y=400)

# Create Label
vagas17_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas17_label.place(x=128,y=400)

# Create Label
vagas18_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas18_label.place(x=208,y=400)

# Create Label
vagas19_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas19_label.place(x=288,y=400)

# Create Label
vagas20_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas20_label.place(x=366,y=400)

# Create Label
vagas21_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas21_label.place(x=444,y=400)

# Create Label
vagas22_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas22_label.place(x=524,y=400)

# Create Label
vagas23_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas23_label.place(x=604,y=400)

# Create Label
vagas24_label = Label(window,
                image = car,
                bg = '#D8D8D8')
                    
vagas24_label.place(x=684,y=400)

client = connect_mqtt()
subscribe(client)
client.loop_start()
 
 
window.mainloop()
client.loop_stop()