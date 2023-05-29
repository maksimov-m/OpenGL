from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

def display():

  glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем серым цветом
  glPushMatrix()# Сохраняем текущее положение "камеры"
  glutSolidCube(3) # Рисуем Куб со сторонами 3х3х3
  glPopMatrix() # Возвращаем сохраненное положение "камеры"
  glutSwapBuffers()# Выводим все нарисованное в памяти на экран





def main():
    glutInit()# Вызываем нашу функцию инициализации
    # Использовать двойную буферизацию и цвета в формате RGB (Красный, Зеленый, Синий)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700,700) # Указываем начальный размер окна (ширина, высота
    glutCreateWindow(b'Cube')
    glClearColor(0.,0.,0.,1.) # цвет для первоначальной закраски

    glutDisplayFunc(display) # Определяем процедуру, отвечающую за перерисовку


    # Функции для корректного отображения
    gluPerspective(50.,1.,1.,40.)
    gluLookAt(0,0,10,
              0,0,0,
              0,1,0)
    glPushMatrix()
    glutMainLoop()# Запускаем основной цикл
    return


main()