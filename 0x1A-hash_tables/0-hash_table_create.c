#include "hash_tables.h"


/**
 * hash_table_create - creates a has table
 * @size: size of the table
 * description: creates a has table
 * Return: table pointer or NULL on failure
*/
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *table;
	hash_node_t **array;

	if (size == 0)
		return (NULL);
	table = malloc(sizeof(hash_table_t));
	if (table == NULL)
		return (NULL);
	array = malloc(sizeof(hash_node_t *) * size);
	if (array == NULL)
	{
		free(table);
		return (NULL);
	}
	table->size = size;
	table->array = array;
	return (table);
}
