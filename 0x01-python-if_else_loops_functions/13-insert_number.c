#include "lists.h"

/**
 * insert_node - inserts node
 * @head: pointer to the head pointer
 * @number: value to insert
 * Return: pointer or null
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *newNode;

	tmp = *head;
	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (0);

	newNode->n = number;
	newNode->next = NULL;
	if ((*head) == NULL)
	{
		*head = newNode;
		return (newNode);
	}
	else if ((*head)->n >= number)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	else 
	{
		while (tmp->next != NULL)
		{
			if (tmp->next->n >= number)
			{
				newNode->next = tmp->next;
				tmp->next = newNode;
				return (newNode);
			}
			tmp = tmp->next;
		}
		newNode->next = NULL;
		tmp->next = newNode;
		return (newNode);
	}
	return (NULL);
}
