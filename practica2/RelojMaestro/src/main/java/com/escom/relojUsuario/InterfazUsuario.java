package com.escom.relojUsuario;

import javax.swing.*;
import java.awt.*;

public class InterfazUsuario extends JFrame {
    private JLabel titulo, hora;
    private JPanel panel;
    private Hilo hiloUsuario;

    public InterfazUsuario () {
        this.setSize(500,200);
        this.setLocationRelativeTo(null);
        this.setTitle("Reloj de usuario");

        construirElementos();

        hiloUsuario = new Hilo(this.hora);
        hiloUsuario.start();

        this.setVisible(true);
    }

    private void construirElementos() {
        panel = new JPanel();
        panel.setLayout(null);
        this.getContentPane().add(panel);

        titulo = new JLabel("Hora del servidor");
        titulo.setFont(new Font("Arial",1,22));
        titulo.setBounds(145,20,500,24);
        panel.add(titulo);

        hora = new JLabel("00:00:00");
        hora.setFont(new Font("Arial",3,30));
        hora.setBounds(180,100,500,30);
        panel.add(hora);
    }
}
