package com.asistente.core.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.mongodb.config.AbstractMongoConfiguration;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;

import com.mongodb.MongoClient;

@Configuration
@EnableMongoRepositories(basePackages = "com.asistente.core.repository")
public class MongoConfig extends AbstractMongoConfiguration {

	@Override
	public MongoClient mongoClient() {
		return new MongoClient("localhost", 27017);
	}

	@Bean
	@Override
	protected String getDatabaseName() {
		return "AsistenteVirtual";
	}

}
