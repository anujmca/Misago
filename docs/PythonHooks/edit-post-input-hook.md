# `edit_post_input_hook`

```python
edit_post_hook.call_action(
    action: EditPostInputAction,
    context: GraphQLContext,
    validators: Dict[str, List[AsyncValidator]],
    data: EditPostInput,
    errors_list: ErrorsList,
)
```

A filter for the function used to validate data for `EditPostInputModel` GraphQL input type.

Returns a tuple of `data` that should be used to update the post and validation `errors`.


## Required arguments

### `action`

```python
async def validate_input_data(
    context: GraphQLContext,
    validators: Dict[str, List[AsyncValidator]],
    data: EditPostInput,
    errors: ErrorsList,
) -> Tuple[EditPostInput, ErrorsList]:
    ...
```

Next filter or built-in function used to validate edited post input data.


### `context`

```python
GraphQLContext
```

A dict with GraphQL query context.


### `validators`

```python
Dict[str, List[AsyncValidator]]
```

A dict of lists of validators that should be used to validate inputs values.


### `data`

```python
Dict[str, Any]
```

A dict with input data that passed initial cleaning and validation. If any of fields failed initial cleanup and validation, it won't be present in this dict.


### `errors`

```python
ErrorsList
```

List of validation errors found so far. Can be extended using it's `add_error` and `add_root_error` methods.