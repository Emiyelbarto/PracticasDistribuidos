package com.escom.relojUsuario;

import com.escom.sockets.Cliente;

import javax.swing.*;

public class Hilo extends Thread {
    private final JLabel indicador;
    private Cliente cliente;

    public Hilo(JLabel indicador) {
        this.indicador = indicador;
        cliente = new Cliente(this.indicador);
        cliente.start();
    }

    public void run() {
        while(true) {
            try {
                sleep(1000);
                actualizarHora();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    private void actualizarHora() {
        int hora, minuto, segundo;
        String nueva_hora, nuevo_minuto, nuevo_segundo;
        String [] tiempo_separado;

        String tiempo = this.indicador.getText();
        tiempo_separado = tiempo.split(":");

        hora = Integer.parseInt(tiempo_separado[0]);
        minuto = Integer.parseInt(tiempo_separado[1]);
        segundo = Integer.parseInt(tiempo_separado[2]);

        if (segundo + 1 == 60){
            if (minuto + 1 == 60){
                if (hora + 1 == 24){
                    hora = 0;
                    minuto = 0;
                    segundo = 0;
                } else {
                    hora += 1;
                    minuto = 0;
                    segundo = 0;
                }
            } else {
                minuto += 1;
                segundo = 0;
            }
        } else {
            segundo += 1;
        }

        if (hora < 10){
            nueva_hora = "0" + String.valueOf(hora);
        } else {
            nueva_hora = String.valueOf(hora);
        }

        if (minuto < 10){
            nuevo_minuto = "0" + String.valueOf(minuto);
        } else {
            nuevo_minuto = String.valueOf(minuto);
        }

        if (segundo < 10){
            nuevo_segundo = "0" + String.valueOf(segundo);
        } else {
            nuevo_segundo = String.valueOf(segundo);
        }

        this.indicador.setText(nueva_hora + ":" + nuevo_minuto + ":" + nuevo_segundo);
    }
}
