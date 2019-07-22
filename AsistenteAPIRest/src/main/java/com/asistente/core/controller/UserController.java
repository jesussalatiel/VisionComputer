package com.asistente.core.controller;

import java.util.Date;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.asistente.core.repository.UserRepository;
import com.asistente.core.model.UserModel;

@RestController
public class UserController {

	@Autowired
	UserRepository userRepository;

	/* Verficamos que el sistema REST este funcionando */
	@GetMapping(value = "/healthy", produces = "application/json; charset = utf-8")
	public String getHealthy() {
		return "{ \" isWorking\": true }";
	}

	/* Lectura de todos los usuarios */
	@GetMapping(value = "/users")
	public List<UserModel> getUser() {
		List<UserModel> usersList = userRepository.findAll();
		return usersList;
	}

	/* Lectura de solo un usuario con Id */
	@GetMapping(value = "/users/{id}")
	public Optional<UserModel> getUserId(@PathVariable String id) {
		Optional<UserModel> userId = userRepository.findById(id);
		return userId;
	}

	/* Actualizacion de datos por Id */
	@PutMapping(value = "/users/{id}")
	public Optional<UserModel> updateUser(@RequestBody UserModel newUser, @PathVariable String id) {
		Optional<UserModel> optionUser = userRepository.findById(id);
		if (optionUser.isPresent()) {
			UserModel usr = optionUser.get();
			usr.setNombre(newUser.getNombre());
			usr.setMedia(newUser.getMedia());
			usr.setImagen(newUser.getImagen());
			usr.setConocido(newUser.isConocido());
			usr.setFecha(new Date());
			usr.setEmail(newUser.getEmail());
			usr.setUser(newUser.getUser());
			usr.setPassword(newUser.getPassword());
			userRepository.save(usr);
		}
		return optionUser;
	}

	/* Eliminamos a usuario por Id */
	@DeleteMapping(value = "/users/{id}")
	public String deleteUserId(@PathVariable String id) {
		Boolean result = userRepository.existsById(id);
		userRepository.deleteById(id);

		return "{ \" Status \": " + (result ? "Ok !" : "False") + "}";
	}

	/* Agregamos a usuarios nuevos */
	@PostMapping(value = "/users")
	public UserModel addUser(@RequestBody UserModel newUser) {
		UserModel usr = new UserModel(newUser.getId(), newUser.getNombre(), newUser.getMedia(), newUser.getImagen(),
				newUser.isConocido(), new Date(), newUser.getEmail(), newUser.getUser(), newUser.getPassword());
		userRepository.insert(usr);
		return usr;
	}
}
