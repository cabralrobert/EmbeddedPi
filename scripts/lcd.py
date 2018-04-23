import Adafruit_CharLCD as LCD
import socket
import os
import time

# Pinos LCD x Raspberry (GPIO)
lcd_rs        = 18
lcd_en        = 23
lcd_d4        = 12
lcd_d5        = 16
lcd_d6        = 20
lcd_d7        = 21
lcd_backlight = 4

# Define numero de colunas e linhas do LCD
#lcd_colunas = 16
#lcd_linhas  = 2

smiley = (
    0b00100,
    0b01010,
    0b01010,
    0b10001,
    0b10001,
    0b10001,
    0b01110,
    0b00000,
)

# Configuracao para display 20x4
lcd_colunas = 20
lcd_linhas  = 4

# Inicializa o LCD nos pinos configurados acima
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5,
                           lcd_d6, lcd_d7, lcd_colunas, lcd_linhas,
                           lcd_backlight)


lcd.create_char(0, smiley)

lcd.set_cursor(0,0)
# Imprime texto na primeira linha
lcd.message(' Testeeee \n')

# Mostra o endereco IP na segunda linha
lcd.message('Robert \n')

lcd.set_cursor(0,2)

lcd.message('Robert')

lcd.set_cursor(0,3)
lcd.message(unichr(0))


# Aguarda 10 segundos
