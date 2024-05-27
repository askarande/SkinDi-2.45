# common.py

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import pygame.camera
import sqlite3
import tkinter as tk
from tkinter import messagebox, Text
import tensorflow as tf
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import time
import numpy as np
from subprocess import call
import os
from keras.models import load_model
from tensorflow.keras.optimizers import Adam
import cv2