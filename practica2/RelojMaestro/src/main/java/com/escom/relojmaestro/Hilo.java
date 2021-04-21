package com.escom.relojmaestro;

import com.escom.sockets.Servidor;

import javax.swing.*;

public class Hilo extends Thread{
    private InterfazModificar ventanaModificar = null;
    private int threadID;
    private final JLabel indicador;
    private int estado = 0;
    private Servidor refServidor;

    /*
    * Estado -> 0   =   Avanza el reloj
    * Estado -> 1   =   Abrir ventana de editar
    * Estado -> 2   =   Enviar actualizacion
    * */

    
    public Hilo(int id, JLabel indicador, Servidor servidor){
        this.refServidor = servidor;
        this.threadID = id;
        this.indicador = indicador;
    }

    public void run(){
        while(true) {
            try {
                switch (estado) {
                    case 0:
                        sleep(1000);
                        actualizarHora();
                        if (!refServidor.clienteCreado(threadID)) {
                            refServidor.setHoraActual(threadID, indicador.getText());
                        }
                        break;
                    case 1:
                        if (ventanaModificar == null)  {
                            ventanaModificar = new InterfazModificar(threadID, this.indicador.getText());
                        }
                        System.out.println("ventanaModificar.isFinalizo() = " + ventanaModificar.isFinalizo());
                        System.out.println("ventanaModificar.getNuevaHora() = " + ventanaModificar.getNuevaHora());
                        if (ventanaModificar.isFinalizo()) {
                            this.indicador.setText(ventanaModificar.getNuevaHora());
                            this.estado = 0;
                        }
                        break;
                    case 2:
                        refServidor.solicitarMensaje(threadID,indicador.getText());
                        this.estado = 0;
                        break;
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void setEstado(int estado) {
        this.estado = estado;
    }
    
    public void actualizarHora(){
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
