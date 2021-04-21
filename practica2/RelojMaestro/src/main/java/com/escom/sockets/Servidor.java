package com.escom.sockets;

import java.net.*;
import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Servidor extends Thread{
    private int numRelojesConectados = 0;
    private List<Boolean> escribirReloj;
    private List<Boolean> clientesCreado;
    private List<String> nuevaHora;
    private List<String> horaActual;
    private HashMap <Integer, String> relRelojesIP;

    public Servidor() {
        escribirReloj = new ArrayList<>();
        relRelojesIP = new HashMap<>();
        nuevaHora = new ArrayList<>();
        horaActual = new ArrayList<>();
        horaActual.add("00:00:00");
        horaActual.add("00:00:00");
        horaActual.add("00:00:00");

        clientesCreado = new ArrayList<>();
        clientesCreado.add(false);
        clientesCreado.add(false);
        clientesCreado.add(false);
    }

    public void run() {
        DatagramSocket socketUDP = null;
        try {
            socketUDP = new DatagramSocket(6666);
        } catch (SocketException e) {
            e.printStackTrace();
        }
        while (true) {
            try {
                byte[] bufer = new byte[1000];
                while(numRelojesConectados < 3){
                    DatagramPacket peticion = new DatagramPacket(bufer, bufer.length);

                    socketUDP.receive(peticion);
                    String ip_cliente = new String(peticion.getData(), 0, peticion.getLength());

                    System.out.println("Ip recibida = " + ip_cliente);

                    escribirReloj.add(false);
                    relRelojesIP.put(numRelojesConectados, ip_cliente);
                    clientesCreado.set(numRelojesConectados, true);

                    enviarHora(horaActual.get(numRelojesConectados),ip_cliente);
                    numRelojesConectados++;
                }

                for(int i = 0; i < 3; i++) {
                    if (escribirReloj.get(i)) {
                        enviarHora(nuevaHora.get(i), relRelojesIP.get(i));
                        escribirReloj.set(i, false);
                    }
                }

            } catch (SocketException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public boolean clienteCreado(int hiloId){
        return clientesCreado.get(hiloId);
    }

    public void setHoraActual(int hiloId, String nuevaHora) {
        this.horaActual.set(hiloId, nuevaHora);
    }

    public void enviarHora(String hora, String ip) throws IOException {
        DatagramSocket socketUDP = new DatagramSocket();
        byte[] mensaje = hora.getBytes();
        InetAddress hostServidor = InetAddress.getByName(ip);
        int puertoServidor = 6666;

        DatagramPacket peticion = new DatagramPacket(mensaje, hora.length(), hostServidor, puertoServidor);
        socketUDP.send(peticion);

        socketUDP.close();
    }

    public void solicitarMensaje(int hiloId, String hora) {
        escribirReloj.set(hiloId, true);
        nuevaHora.set(hiloId, hora);
    }
}
