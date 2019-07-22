package com.asistente.core.repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.asistente.core.model.UserModel;

public interface UserRepository extends MongoRepository<UserModel, String> {

}
