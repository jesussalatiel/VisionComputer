package com.asistente.core.model;

import java.io.Serializable;
import java.util.Date;

import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@AllArgsConstructor
@Setter
@Getter
@Document(collection = "Users")
public class UserModel implements Serializable {

	@Id
	private String id = null;
	private String nombre = null;
	private String media = null;
	private String imagen = null;
	private boolean conocido = false;
	private Date fecha = null;
	private String email = null;
	private String user = null;
	private String password = null;

	public UserModel(String id, String nombre, String media, String imagen, boolean conocido, Date fecha, String email,
			String user, String password) {
		this.id = id;
		this.nombre = nombre;
		this.media = media;
		this.imagen = imagen;
		this.conocido = conocido;
		this.fecha = fecha;
		this.email = email;
		this.user = user;
		this.password = password;
	}

	public UserModel() {

	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getMedia() {
		return media;
	}

	public void setMedia(String media) {
		this.media = media;
	}

	public String getImagen() {
		return imagen;
	}

	public void setImagen(String imagen) {
		this.imagen = imagen;
	}

	public boolean isConocido() {
		return conocido;
	}

	public void setConocido(boolean conocido) {
		this.conocido = conocido;
	}

	public Date getFecha() {
		return fecha;
	}

	public void setFecha(Date fecha) {
		this.fecha = fecha;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getUser() {
		return user;
	}

	public void setUser(String user) {
		this.user = user;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

}
