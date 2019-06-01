import csv
import numpy as np
from scipy import signal
import control
import Tkinter
import sys
import matplotlib.pyplot as plt



fpl = 1e3   # pass low
fph = 1e6   # pass high
fsl = 60    # stop low
fsh = 10e6  # stop high

# especificado
ripple_pass = 1

# calculado para n de bits igual a 12
ripple_rej = 73

# calcula ordem e freq central
N, Wn = signal.cheb1ord([2*np.pi*fpl, 2*np.pi*fph], [2*np.pi*fsl, 2*np.pi*fsh], ripple_pass, ripple_rej, analog=True)

# gera a func de transferencia
num, den = signal.cheby1(N, 1, Wn, 'bandpass', analog=True)

# calcula polos, zeros e ganho
z, p, k = signal.tf2zpk(num, den)

# salva esses dados em um arquivo csv, uma vez que esses dados
# sao usados depois para o calculo dos componentes do circuito
out = open('out.csv', 'w')
out.write(str(k) + ',\n')
for i in p:
	out.write(str(i) + ',')
out.write('\n')
for i in z:
	out.write(str(i) + ',')
out.write('\n')

# calcula a resposta em freq
w, h = signal.freqs(num, den, worN=np.logspace(-1, 9, 1000))

# plota a amplitude
plt.semilogx(w/(2*np.pi), 20 * np.log10(abs(h)))
plt.grid(which='both', axis='both')
plt.title('Chebyshev 1 db, N = ' + str(N) + ', Fpl = ' + str(int(fpl)) + ' hz, Fph = ' + str(int(fph)) + ' hz')
plt.xlabel('Frequencia [hz]')
plt.ylabel('Amplitude [dB]')
plt.axis([10, 100000000, -150, 3])
plt.fill([.01, 60, 60, .01], [-73, -73, -250, -250], '0.5')
plt.fill([10e6, 10e8, 10e8, 10e6], [-73, -73, -250, -250], '0.5')
plt.savefig('amp1.pdf')
plt.clf()

# plota a amplitude, com zoom na faixa de passagem
plt.title('Chebyshev 1 db, N = ' + str(N) + ', Fpl = ' + str(int(fpl)) + ' hz, Fph = ' + str(int(fph)) + ' hz')
plt.semilogx(w/(2*np.pi), 20 * np.log10(abs(h)))
plt.grid(which='both', axis='both')
plt.xlabel('Frequencia [hz]')
plt.ylabel('Amplitude [dB]')
plt.axis([0.8e3, 1.2e6, -4, 2])
plt.fill([1e3, 1e6, 1e6, 1e3], [0, 0, -1, -1], '0.5')
plt.savefig('amp2.pdf')
plt.clf()

# plota a fase
phase = np.unwrap(np.angle(h))
plt.semilogx(w/(2*np.pi), phase*180/np.pi)
plt.axis([10, 1e8, -720, 0])
plt.grid(which='both', axis='both')
plt.title('Chebyshev 1 db, N = ' + str(N) + ', Fpl = ' + str(int(fpl)) + ' hz, Fph = ' + str(int(fph)) + ' hz')
plt.xlabel('Frequencia [hz]')
plt.ylabel('Fase [graus]')
plt.savefig('fase.pdf')
plt.clf()

gp_y=[]
gp_x=[]
for i in range(len(w)-1):
	gp_y.append (-(phase[i+1]-phase[i])/(w[i+1]-w[i]))
	gp_x.append(w[i+1]/(2*np.pi))
plt.semilogx(gp_x, gp_y)
plt.axis([10, 1e8, 0, 0.0013])
plt.grid(which='both', axis='both')
plt.title('Chebyshev 1 db, N = ' + str(N) + ', Fpl = ' + str(int(fpl)) + ' hz, Fph = ' + str(int(fph)) + ' hz')
plt.xlabel('Frequencia [hz]')
plt.ylabel('Atraso de grupo [s]')
plt.savefig('gdelay.pdf')
plt.clf()


# plot do diagrama de polos e zeros
z_x = []
z_y = []
p_x = []
p_y = []
for i in z:
	z_x.append(np.real(i))
	z_y.append(np.imag(i))
for i in p:
	p_x.append(np.real(i))
	p_y.append(np.imag(i))

# zoom nos polos passa-alta
plt.scatter(z_x, z_y, s=40, facecolors='none', edgecolors='k')
plt.scatter(p_x, p_y, marker='x', color='black')
plt.title('Chebyshev 1 db, N = ' + str(N) + ', Fpl = ' + str(int(fpl)) + ' hz, Fph = ' + str(int(fph)) + ' hz')
plt.xlabel('Real')
plt.ylabel('Imaginario')
plt.axis([-10000, 1000, -10000, 10000])
plt.grid(which='both', axis='both')
plt.savefig('zpd1.pdf', bbox_inches = "tight")
plt.clf()

# zoom out nos polos passa baixa
plt.scatter(z_x, z_y, s=40, facecolors='none', edgecolors='k')
plt.scatter(p_x, p_y, marker='x', color='black')
plt.title('Chebyshev 1 db, N = ' + str(N) + ', Fpl = ' + str(int(fpl)) + ' hz, Fph = ' + str(int(fph)) + ' hz')
plt.xlabel('Real')
plt.ylabel('Imaginario')
plt.axis([-2500000, 100000, -7000000, 7000000])
plt.grid(which='both', axis='both')	
plt.savefig('zpd2.pdf', bbox_inches = "tight")
plt.clf()

