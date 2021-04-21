package com.escom.sockets;

import javax.swing.*;
import java.net.*;
import java.io.*;
import java.util.Enumeration;

public class Cliente extends Thread{
    private JLabel indicador;

    public Cliente (JLabel indicador) {
        this.indicador = indicador;
    }

    public void run() {
        try {
            DatagramSocket socketUDP = new DatagramSocket(6666);
            byte[] bufer = new byte[1000];

            int num = 0;
            String ip = "";

            Enumeration e = NetworkInterface.getNetworkInterfaces();
            while(e.hasMoreElements()) {
                NetworkInterface n = (NetworkInterface) e.nextElement();
                Enumeration ee = n.getInetAddresses();
                while (ee.hasMoreElements()) {
                    InetAddress i = (InetAddress) ee.nextElement();
                    if(num == 1 ){
                        ip = i.getHostAddress();
                    }
                    num++;
                }
            }

            DatagramSocket enviarIP = new DatagramSocket();
            byte[] mensaje = ip.getBytes();
            InetAddress hostServidor = InetAddress.getByName("192.168.0.178"); // IP DEL SERVIDOR
            int puertoServidor = 6666;
            DatagramPacket ipEnviar = new DatagramPacket(mensaje, ip.length(), hostServidor, puertoServidor);
            enviarIP.send(ipEnviar);
            enviarIP.close();

            while (true) {
                DatagramPacket peticion = new DatagramPacket(bufer, bufer.length);
                socketUDP.receive(peticion);

                String hora_recibida = new String(peticion.getData(), 0, peticion.getLength());

                System.out.println("Hora recibida por el servidor = " + hora_recibida);

                this.indicador.setText(hora_recibida);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
