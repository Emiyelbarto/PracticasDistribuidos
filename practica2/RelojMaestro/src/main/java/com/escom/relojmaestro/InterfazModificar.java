package com.escom.relojmaestro;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class InterfazModificar extends JFrame {
    private String tiempoActual, nuevaHora;
    private JPanel panel;
    private JLabel titulo;
    private JSpinner sp_hora, sp_minuto, sp_segundo;
    private JButton guardar;
    private JLabel puntos, puntos2;
    private boolean finalizo = false;

    public InterfazModificar(int relojId, String tiempoActual) {
        this.tiempoActual = tiempoActual;
        this.setSize(500,320);
        this.setLocationRelativeTo(null);
        this.setTitle("Editar hora del reloj: " + (relojId + 1));

        construirElementos();

        this.setVisible(true);
    }

    public void construirElementos() {
        SpinnerNumberModel modelo24 = new SpinnerNumberModel(0, 0, 23, 1);
        SpinnerNumberModel modelo60 = new SpinnerNumberModel(0, 0, 59, 1);
        SpinnerNumberModel modelo60s = new SpinnerNumberModel(0, 0, 59, 1);
        int hora, minuto, segundo;

        String [] tiempo_separado;

        tiempo_separado = tiempoActual.split(":");

        hora = Integer.parseInt(tiempo_separado[0]);
        minuto = Integer.parseInt(tiempo_separado[1]);
        segundo = Integer.parseInt(tiempo_separado[2]);

        panel = new JPanel();
        panel.setLayout(null);
        this.getContentPane().add(panel);

        titulo = new JLabel("Selecciona una nueva hora");
        titulo.setFont(new Font("Arial",1,22));
        titulo.setBounds(85,20,500,24);
        panel.add(titulo);

        sp_hora = new JSpinner(modelo24);
        sp_hora.setValue(hora);
        sp_hora.setBounds(100,100,50,30);
        panel.add(sp_hora);

        puntos = new JLabel(":");
        puntos.setBounds(188,100,10,30);
        panel.add(puntos);

        sp_minuto = new JSpinner(modelo60);
        sp_minuto.setValue(minuto);
        sp_minuto.setBounds(225,100,50,30);
        panel.add(sp_minuto);

        puntos2 = new JLabel(":");
        puntos2.setBounds(313,100,10,30);
        panel.add(puntos2);

        sp_segundo = new JSpinner(modelo60s);
        sp_segundo.setValue(segundo);
        sp_segundo.setBounds(350,100,50,30);
        panel.add(sp_segundo);

        guardar = new JButton("Guardar");
        guardar.setBounds(200,200,100,30);
        guardar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String nHora, nMinuto, nSegundo;
                nHora = sp_hora.getValue().toString();
                nMinuto = sp_minuto.getValue().toString();
                nSegundo = sp_segundo.getValue().toString();

                if (nHora.length() == 1) {
                    nHora = "0" + nHora;
                }
                if (nMinuto.length() == 1) {
                    nMinuto = "0" + nMinuto;
                }
                if (nSegundo.length() == 1) {
                    nSegundo = "0" + nSegundo;
                }
                setNuevaHora(nHora + ":" + nMinuto + ":" + nSegundo);
                setFinalizo(true);
                hide();
            }
        });

        panel.add(guardar);
    }

    public boolean isFinalizo(){
        return finalizo;
    }

    public void setNuevaHora(String nuevaHora) {
        this.nuevaHora = nuevaHora;
    }

    public void setFinalizo(boolean finalizo) {
        this.finalizo = finalizo;
    }

    public String getNuevaHora(){
        return nuevaHora;
    }
}
