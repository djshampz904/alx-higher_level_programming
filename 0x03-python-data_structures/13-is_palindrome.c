#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palidrome
 * @head: pointer to the head pointer to the list
 * Return: integer
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
	{
		return (0);
	}

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *prev = NULL;
	listint_t *curr = slow;
	listint_t *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	listint_t *left = *head;
	listint_t *right = prev;

	while (right != NULL)
	{
		if (left->n != right->n)
		{
			return (0);
		}
		left = left->next;
		right = right->next;
	}

	return (1);
}
